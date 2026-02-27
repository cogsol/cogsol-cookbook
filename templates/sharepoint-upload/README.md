# SharePoint Upload

A starting point for building a CogSol agent that generates text documents and uploads them to a SharePoint document library.

The agent receives a user request, generates the document content, and uses a script tool to upload it via the Microsoft Graph API. Authentication uses the OAuth2 client credentials flow with Azure AD.

> **See also:** The [`sharepoint-excel`](../sharepoint-excel/README.md) template reads data from Excel files in SharePoint using the same authentication pattern.

## Use Case

You need an agent that produces text-based content (reports, summaries, notes, etc.) and stores it in a SharePoint document library without leaving the conversation.

This template provides the upload tool ready to use. You only need to:

1. **Register an Azure AD application** with permissions to write to SharePoint.
2. **Configure your credentials** as platform secrets.
3. **Customize the agent prompt** in `agents/sharepointupload/prompts/sharepointupload.md` to fit your domain.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- An [Azure AD app registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) with:
  - **Application (client) ID** and **client secret**
  - API permission: `Files.ReadWrite.All` (application type, admin-consented)
- A SharePoint site where the agent will upload files

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `UploadToSharePoint` script tool that authenticates with Azure AD and uploads files via Graph API |
| `agents/sharepointupload/agent.py` | Agent definition with the upload tool |
| `agents/sharepointupload/prompts/sharepointupload.md` | System prompt for the agent (customize this) |

### How the Script Tool Works

The `UploadToSharePoint` tool:

1. Requests an OAuth2 access token from Azure AD using the client credentials flow.
2. Sends a `PUT` request to the Microsoft Graph API to upload the content to the SharePoint document library.
3. Returns the SharePoint URL of the uploaded file on success or an error message on failure.

This approach works for files up to 4 MB. For larger files, use an [upload session](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession).

No external libraries are required. The tool uses only the Python standard library (`urllib`, `json`).

### Finding Your Site ID and Drive ID

You need the SharePoint site ID and document library drive ID to configure the secrets. Use the [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) or these API calls:

```bash
# Get site ID (replace with your SharePoint domain and site path)
GET https://graph.microsoft.com/v1.0/sites/{hostname}:/{site-path}

# Get drive ID (list document libraries for the site)
GET https://graph.microsoft.com/v1.0/sites/{site-id}/drives
```

## Getting Started

### Step 1. Configure your environment

```bash
cd templates/sharepoint-upload
cp .env.example .env
```

Edit `.env` and fill in your CogSol API credentials.

### Step 2. Configure platform secrets

Create the following secrets in your CogSol tenant:

| Secret name | Value |
|-------------|-------|
| `AZURE_TENANT_ID` | Your Azure AD tenant ID |
| `AZURE_CLIENT_ID` | Application (client) ID from the app registration |
| `AZURE_CLIENT_SECRET` | Client secret value |
| `SHAREPOINT_SITE_ID` | SharePoint site ID (see above) |
| `SHAREPOINT_DRIVE_ID` | Document library drive ID (see above) |

### Step 3. Customize the system prompt

Edit `agents/sharepointupload/prompts/sharepointupload.md`. For example, if generating meeting minutes:

```markdown
# Meeting Minutes Assistant

You generate structured meeting minutes and upload them to SharePoint.
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
python manage.py chat --agent SharePointUploadAgent
```

Try a message like:

> Generate a summary of our product launch plan and save it as launch-plan.txt

The agent will generate the content, authenticate with Azure AD, and upload the file to your SharePoint document library.

## Customization Notes

- **Different content types**: Change the `Content-Type` header in `agents/tools.py` to upload JSON, CSV, HTML, or other text formats.
- **Upload to subfolders**: Change the Graph API path from `/root:/{filename}:/content` to `/root:/{folder}/{filename}:/content`.
- **Large files (> 4 MB)**: Replace the simple PUT with an [upload session](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession) for chunked uploads.
- **Combine with reading**: Add the `QuerySharePointExcel` tool from the [`sharepoint-excel`](../sharepoint-excel/README.md) template to build an agent that both reads and writes SharePoint files.
- **Add retrieval**: Uncomment the scaffold files in `data/` and `agents/searches.py` to add semantic search. See the [`semantic-search`](../semantic-search/README.md) template.
