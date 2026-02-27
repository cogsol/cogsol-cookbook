# Azure Storage Upload

A starting point for building a CogSol agent that generates text documents and uploads them to Azure Blob Storage.

The agent receives a user request, generates the document content, and uses a script tool to upload it directly to a storage account via the Azure Blob Storage REST API. Authentication is handled with a SAS token stored in the platform secrets.

## Use Case

You need an agent that produces text-based content (reports, summaries, notes, configuration files, etc.) and stores it in Azure Blob Storage without leaving the conversation.

This template provides the upload tool ready to use. You only need to:

1. **Configure your Azure credentials** as platform secrets.
2. **Customize the agent prompt** in `agents/azurestorageupload/prompts/azurestorageupload.md` to fit your domain.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- An Azure Storage Account with a container and a [SAS token](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) that has write permissions

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `UploadToAzureStorage` script tool that uploads content to Azure Blob Storage |
| `agents/azurestorageupload/agent.py` | Agent definition with the upload tool |
| `agents/azurestorageupload/prompts/azurestorageupload.md` | System prompt for the agent (customize this) |

### How the Script Tool Works

The `UploadToAzureStorage` tool:

1. Reads Azure credentials from **platform secrets** (`AZURE_STORAGE_ACCOUNT`, `AZURE_CONTAINER_NAME`, `AZURE_SAS_TOKEN`).
2. Builds the Blob Storage REST API URL with the SAS token.
3. Sends a `PUT` request using Python's `urllib` to upload the content as a block blob.
4. Returns the blob URL on success or an error message on failure.

No external libraries are required. The tool uses only the Python standard library.

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
| `AZURE_STORAGE_ACCOUNT` | Your storage account name (e.g. `mystorageaccount`) |
| `AZURE_CONTAINER_NAME` | The target container name (e.g. `documents`) |
| `AZURE_SAS_TOKEN` | A SAS token with write permission to the container |

> **Tip:** Generate the SAS token from the Azure Portal under your storage account > Shared access signature. Include at least the **Blob** service, **Object** resource type, and **Write** permission.

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

The agent will generate the content and upload it to your Azure Blob Storage container.

## Customization Notes

- **Different content types**: Change the `Content-Type` header in `agents/tools.py` to upload JSON (`application/json`), CSV (`text/csv`), HTML (`text/html`), or other text formats.
- **Dynamic containers**: Add a `container` parameter to the tool so the LLM can choose the target container at runtime.
- **Azure AD authentication**: Replace the SAS token approach with an OAuth2 client credentials flow. Request a token from `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token` and use it as a Bearer token in the `Authorization` header.
- **Add retrieval**: Uncomment the scaffold files in `data/` and `agents/searches.py` to add semantic search capabilities. See the [`semantic-search`](../semantic-search/README.md) template for the full pattern.
