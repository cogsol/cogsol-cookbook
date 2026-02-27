# SharePoint Excel Query

A starting point for building a CogSol agent that reads data from Excel files hosted in SharePoint.

The agent receives a user request, identifies the target file, worksheet, and cell range, and uses a script tool to fetch the data via the Microsoft Graph API. Authentication uses the OAuth2 client credentials flow with Azure AD.

## Use Case

You have Excel files stored in a SharePoint document library and want an agent that can query specific ranges and return the data in conversation, without the user needing direct access to SharePoint.

This template provides the query tool ready to use. You only need to:

1. **Register an Azure AD application** with permissions to read SharePoint files.
2. **Configure your credentials** as platform secrets.
3. **Customize the agent prompt** in `agents/sharepointexcel/prompts/sharepointexcel.md` to fit your domain.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- An [Azure AD app registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) with:
  - **Application (client) ID** and **client secret**
  - API permission: `Sites.Read.All` (application type, admin-consented)
- A SharePoint site with the target Excel file(s)

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `QuerySharePointExcel` script tool that authenticates with Azure AD and reads Excel ranges via Graph API |
| `agents/sharepointexcel/agent.py` | Agent definition with the query tool |
| `agents/sharepointexcel/prompts/sharepointexcel.md` | System prompt for the agent (customize this) |

### How the Script Tool Works

The `QuerySharePointExcel` tool:

1. Requests an OAuth2 access token from Azure AD using the client credentials flow.
2. Calls the Microsoft Graph API to read the specified worksheet range from the Excel file.
3. Formats the cell values as a readable text table and returns them to the agent.

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
cd templates/sharepoint-excel
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

Edit `agents/sharepointexcel/prompts/sharepointexcel.md`. For example, if querying financial reports:

```markdown
# Financial Data Assistant

You help users retrieve data from financial Excel reports stored in SharePoint.
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
python manage.py chat --agent SharePointExcelAgent
```

Try a message like:

> Show me the data from sales-report.xlsx, Sheet1, range A1:E5

The agent will authenticate with Azure AD, query the Graph API, and return the cell values.

## Customization Notes

- **List available files**: Add a second script tool that calls `GET /sites/{site-id}/drives/{drive-id}/root/children` to let the agent browse the document library.
- **Write data back**: Use `PATCH /workbook/worksheets('{sheet}')/range(address='{range}')` with a JSON body containing the `values` array to update cells.
- **Multiple sites**: Add a `site` parameter to the tool and store multiple site/drive ID pairs as secrets.
- **Delegated access**: Replace client credentials with delegated auth if you need per-user permissions instead of app-level access.
- **Add retrieval**: Uncomment the scaffold files in `data/` and `agents/searches.py` to add semantic search. See the [`semantic-search`](../semantic-search/README.md) template.
