from cogsol.tools import BaseTool, tool_params


class QuerySharePointExcel(BaseTool):
    """Script tool that reads data from an Excel file hosted in SharePoint."""

    name = "query_sharepoint_excel"
    description = (
        "Read data from an Excel file stored in SharePoint. "
        "Specify the file name, worksheet, and cell range to retrieve."
    )
    show_tool_message = False

    @tool_params(
        filename={
            "description": "Name of the Excel file in SharePoint (e.g. sales-report.xlsx).",
            "type": "string",
            "required": True,
        },
        sheet={
            "description": "Worksheet name to read from (e.g. Sheet1).",
            "type": "string",
            "required": True,
        },
        cell_range={
            "description": "Cell range to retrieve (e.g. A1:D10).",
            "type": "string",
            "required": True,
        },
    )
    def run(self, filename="", sheet="", cell_range="", chat=None, data=None, secrets=None, log=None):
        from urllib import request, error, parse
        import json

        tenant_id = secrets.get("AZURE_TENANT_ID", "")
        client_id = secrets.get("AZURE_CLIENT_ID", "")
        client_secret = secrets.get("AZURE_CLIENT_SECRET", "")
        site_id = secrets.get("SHAREPOINT_SITE_ID", "")
        drive_id = secrets.get("SHAREPOINT_DRIVE_ID", "")

        if not all([tenant_id, client_id, client_secret, site_id, drive_id]):
            return "Missing SharePoint configuration. Check platform secrets."

        # Step 1: Get OAuth2 access token
        token_url = (
            f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        )
        token_data = parse.urlencode({
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "https://graph.microsoft.com/.default",
        }).encode("utf-8")

        log.append("Requesting access token...")
        try:
            token_req = request.Request(
                token_url, data=token_data, method="POST"
            )
            with request.urlopen(token_req) as resp:
                token_body = json.loads(resp.read().decode("utf-8"))
                access_token = token_body["access_token"]
        except error.HTTPError as e:
            log.append(f"Token request failed: {e.code}")
            return f"Authentication failed: {e.code} {e.reason}"
        except (KeyError, json.JSONDecodeError) as e:
            log.append(f"Token parsing error: {str(e)}")
            return "Authentication failed: could not parse token response."

        # Step 2: Query Excel range via Microsoft Graph API
        encoded_filename = parse.quote(filename)
        encoded_sheet = parse.quote(sheet)
        encoded_range = parse.quote(cell_range)

        graph_url = (
            f"https://graph.microsoft.com/v1.0"
            f"/sites/{site_id}/drives/{drive_id}"
            f"/root:/{encoded_filename}:"
            f"/workbook/worksheets('{encoded_sheet}')"
            f"/range(address='{encoded_range}')"
        )

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        }

        log.append(f"Querying {filename} [{sheet}!{cell_range}]...")
        try:
            graph_req = request.Request(graph_url, headers=headers, method="GET")
            with request.urlopen(graph_req) as resp:
                body = json.loads(resp.read().decode("utf-8"))
        except error.HTTPError as e:
            log.append(f"Graph API error: {e.code}")
            body_text = e.read().decode("utf-8") if hasattr(e, "read") else ""
            return f"Failed to read Excel data: {e.code} {e.reason}\n{body_text}"
        except error.URLError as e:
            log.append(f"Connection error: {str(e)}")
            return f"Connection error: {str(e)}"

        # Step 3: Format the response
        values = body.get("values", [])
        if not values:
            return f"No data found in {filename} [{sheet}!{cell_range}]."

        # Build a readable text table
        lines = []
        for row in values:
            line = " | ".join(str(cell) if cell is not None else "" for cell in row)
            lines.append(line)

        log.append(f"Retrieved {len(values)} rows")
        header = f"Data from {filename} [{sheet}!{cell_range}]:\n"
        return header + "\n".join(lines)
