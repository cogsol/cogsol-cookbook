#!/usr/bin/env python3
"""Ingest knowledge base articles with metadata into the Content API.

The standard ``manage.py ingest`` command does not support per-document
metadata, so this script uploads each article individually and attaches
its category metadata.

Usage:
    python scripts/ingest_knowledgebase.py
"""

import json
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from cogsol.core.env import load_dotenv
from cogsol.core.api import CogSolClient

load_dotenv(PROJECT_DIR / ".env")

# ---------------------------------------------------------------------------
# Knowledge base articles: filename -> metadata values
# ---------------------------------------------------------------------------
ARTICLES = {
    "network-troubleshooting.md": {"category": "Network"},
    "printer-setup.md": {"category": "Hardware"},
    "software-licenses.md": {"category": "Software"},
    "video-conferencing.md": {"category": "Software"},
    "security-best-practices.md": {"category": "Security"},
    "data-backup-recovery.md": {"category": "Security"},
    "new-employee-onboarding.md": {"category": "Onboarding"},
    "remote-work-setup.md": {"category": "Onboarding"},
}

DOCS_DIR = PROJECT_DIR / "data" / "knowledgebase" / "docs"


def load_state():
    """Read remote IDs from the data migrations state file."""
    state_path = PROJECT_DIR / "data" / "migrations" / ".state.json"
    if not state_path.exists():
        print("ERROR: data/migrations/.state.json not found. Run 'manage.py migrate data' first.")
        sys.exit(1)
    data = json.loads(state_path.read_text(encoding="utf-8"))
    return data.get("remote", {})


def resolve_metadata_config_ids(client, node_id):
    """Fetch metadata config IDs from the Content API."""
    configs = client.request("GET", f"/nodes/{node_id}/metadata_configs/", use_content_api=True)
    return {cfg["name"]: cfg["id"] for cfg in configs}


def main():
    remote = load_state()

    node_id = remote.get("topics", {}).get("knowledgebase")
    if not node_id:
        print("ERROR: 'knowledgebase' topic not found in state. Run 'manage.py migrate data' first.")
        sys.exit(1)

    ingestion_config_id = remote.get("ingestion_configs", {}).get("helpdesk_ingestion")

    client = CogSolClient()
    config_ids = resolve_metadata_config_ids(client, node_id)

    succeeded = 0
    failed = 0

    for filename, meta_values in ARTICLES.items():
        file_path = DOCS_DIR / filename
        if not file_path.exists():
            print(f"  SKIP {filename}: file not found")
            failed += 1
            continue

        metadata = []
        for field_name, value in meta_values.items():
            config_id = config_ids.get(field_name)
            if config_id:
                metadata.append({"key": field_name, "values": [value], "metadata_config": config_id})

        try:
            doc_id = client.upload_document(
                file_path=str(file_path),
                name=file_path.name,
                node_id=node_id,
                doc_type="Markdown",
                metadata=metadata,
                ingestion_config_id=ingestion_config_id,
            )
            print(f"  OK {filename} -> document_id={doc_id}")
            succeeded += 1
        except Exception as exc:
            print(f"  ERR {filename}: {exc}")
            failed += 1

    print(f"\nIngestion complete: {succeeded} succeeded, {failed} failed.")


if __name__ == "__main__":
    main()
