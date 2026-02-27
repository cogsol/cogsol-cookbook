# Azure Storage Upload

A starting point for building a CogSol agent that generates text documents and uploads them to Azure Blob Storage.

The agent receives a user request, generates the document content, and uses a script tool to upload it to a storage account using the `azure.storage.blob` SDK. After uploading, the tool generates a temporary SAS URL so the user can download the file directly.

## Use Case

You need an agent that produces text-based content (reports, summaries, notes, configuration files, etc.) and stores it in Azure Blob Storage without leaving the conversation.

This template provides the upload tool ready to use. You only need to:

1. **Configure your Azure credentials** as platform secrets.
2. **Customize the agent prompt** in `agents/azurestorageupload/prompts/azurestorageupload.md` to fit your domain.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- An Azure Storage Account with a container and an access key

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `UploadToAzureStorage` script tool that uploads content to Azure Blob Storage |
| `agents/azurestorageupload/agent.py` | Agent definition with the upload tool |
| `agents/azurestorageupload/prompts/azurestorageupload.md` | System prompt for the agent (customize this) |

### How the Script Tool Works

The `UploadToAzureStorage` tool:

1. Reads Azure credentials from **platform secrets** (`AZURE_ACCOUNT_NAME`, `AZURE_ACCOUNT_KEY`, `AZURE_CONTAINER_NAME`).
2. Connects to the storage account using `BlobServiceClient` with a connection string.
3. Uploads the content as a blob using `upload_blob()`.
4. Generates a temporary SAS URL (valid for 60 minutes) so the user can download the file.
5. Returns the SAS URL on success or an error message on failure.

## Getting Started

### Step 1. Configure your environment

```bash
cd templates/azure-storage-upload
cp .env.example .env
```

Edit `.env` and fill in your CogSol API credentials.

### Step 2. Configure platform secrets

The script tool reads Azure credentials from [platform secrets](https://docs.cogsol.ai). Create the following secrets in your CogSol tenant:

| Secret name | Value |
|-------------|-------|
| `AZURE_ACCOUNT_NAME` | Your storage account name (e.g. `mystorageaccount`) |
| `AZURE_ACCOUNT_KEY` | One of the two access keys from the storage account |
| `AZURE_CONTAINER_NAME` | The target container name (e.g. `documents`) |

> **Tip:** Find the access keys in the Azure Portal under your storage account > Access keys.

### Step 3. Customize the system prompt

Edit `agents/azurestorageupload/prompts/azurestorageupload.md` to describe the agent's role. For example, if the agent generates meeting notes:

```markdown
# Meeting Notes Assistant

You generate structured meeting notes and upload them to cloud storage.
```

### Step 4. Deploy

```bash
# Generate migrations
python manage.py makemigrations

# Deploy agent to CogSol API
python manage.py migrate agents
```

### Step 5. Test

```bash
python manage.py chat --agent AzureStorageUploadAgent
```

Try a message like:

> Generate a summary of the key points from our Q4 planning session and save it as q4-planning.txt

The agent will generate the content, upload it, and return a temporary download URL.

## Customization Notes

- **Different content types**: Change the `content_type` in `ContentSettings` inside `agents/tools.py` to upload JSON (`application/json`), CSV (`text/csv`), HTML (`text/html`), or other formats.
- **Subdirectories**: Prefix the filename with a path (e.g. `reports/q4-planning.txt`) to organize blobs into virtual directories.
- **SAS expiry**: Adjust `timedelta(minutes=60)` in `agents/tools.py` to change how long the download URL stays valid.
- **Overwrite behavior**: The tool uses `overwrite=True` by default. Set it to `False` if you want to prevent replacing existing blobs.
- **Add retrieval**: Uncomment the scaffold files in `data/` and `agents/searches.py` to add semantic search capabilities. See the [`semantic-search`](../semantic-search/README.md) template for the full pattern.
