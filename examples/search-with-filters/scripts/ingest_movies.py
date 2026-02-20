#!/usr/bin/env python3
"""Ingest movie documents with metadata into the Content API.

The standard ``manage.py ingest`` command does not support per-document
metadata, so this script uploads each movie file individually and
attaches genre, language, and decade metadata.

Usage:
    python scripts/ingest_movies.py
"""

import json
import sys
from pathlib import Path

# Resolve project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from cogsol.core.env import load_dotenv
from cogsol.core.api import CogSolClient

load_dotenv(PROJECT_DIR / ".env")

# ---------------------------------------------------------------------------
# Movie catalog: filename -> metadata values
# ---------------------------------------------------------------------------
MOVIES = {
    "the-shawshank-redemption.md": {"genre": "Drama", "language": "English", "decade": "1990s"},
    "pulp-fiction.md": {"genre": "Thriller", "language": "English", "decade": "1990s"},
    "spirited-away.md": {"genre": "Animation", "language": "Japanese", "decade": "2000s"},
    "amelie.md": {"genre": "Comedy", "language": "French", "decade": "2000s"},
    "the-dark-knight.md": {"genre": "Action", "language": "English", "decade": "2000s"},
    "pans-labyrinth.md": {"genre": "Drama", "language": "Spanish", "decade": "2000s"},
    "inception.md": {"genre": "Sci-Fi", "language": "English", "decade": "2010s"},
    "parasite.md": {"genre": "Thriller", "language": "Korean", "decade": "2010s"},
    "get-out.md": {"genre": "Horror", "language": "English", "decade": "2010s"},
    "the-grand-budapest-hotel.md": {"genre": "Comedy", "language": "English", "decade": "2010s"},
    "dune.md": {"genre": "Sci-Fi", "language": "English", "decade": "2020s"},
    "everything-everywhere.md": {"genre": "Action", "language": "English", "decade": "2020s"},
}

DOCS_DIR = PROJECT_DIR / "data" / "movies" / "docs"


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

    node_id = remote.get("topics", {}).get("movies")
    if not node_id:
        print("ERROR: 'movies' topic not found in state. Run 'manage.py migrate data' first.")
        sys.exit(1)

    ingestion_config_id = remote.get("ingestion_configs", {}).get("movie_ingestion")

    client = CogSolClient()
    config_ids = resolve_metadata_config_ids(client, node_id)

    succeeded = 0
    failed = 0

    for filename, meta_values in MOVIES.items():
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
