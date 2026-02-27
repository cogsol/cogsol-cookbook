from cogsol.tools import BaseTool, tool_params


class UploadToSharePoint(BaseTool):
    """Script tool that uploads a text document to a SharePoint document library."""

    name = "upload_to_sharepoint"
    description = (
        "Upload a text document to SharePoint. "
        "Use this to save generated content as a file in a SharePoint document library."
    )
    show_tool_message = False

    @tool_params(
        content={
            "description": "The document content to upload.",
            "type": "string",
            "required": True,
        },
        filename={
            "description": (
                "Name for the file in SharePoint, including extension "
                "(e.g. report.txt, summary.md)."
            ),
            "type": "string",
            "required": True,
        },
    )
    def run(self, content="", filename="", chat=None, data=None, secrets=None, log=None):
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

        # Step 2: Upload file via Microsoft Graph API
        encoded_filename = parse.quote(filename)
        graph_url = (
            f"https://graph.microsoft.com/v1.0"
            f"/sites/{site_id}/drives/{drive_id}"
            f"/root:/{encoded_filename}:/content"
        )

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "text/plain; charset=utf-8",
        }

        log.append(f"Uploading {filename} to SharePoint...")
        try:
            graph_req = request.Request(
                graph_url,
                data=content.encode("utf-8"),
                headers=headers,
                method="PUT",
            )
            with request.urlopen(graph_req) as resp:
                body = json.loads(resp.read().decode("utf-8"))
                web_url = body.get("webUrl", "")
                log.append(f"Upload successful: {resp.status}")
                return (
                    f"Document uploaded successfully to SharePoint.\n\n"
                    f"File: {filename}\n"
                    f"URL: {web_url}"
                )
        except error.HTTPError as e:
            log.append(f"Upload failed: {e.code}")
            body_text = e.read().decode("utf-8") if hasattr(e, "read") else ""
            return f"Upload failed: {e.code} {e.reason}\n{body_text}"
        except error.URLError as e:
            log.append(f"Connection error: {str(e)}")
            return f"Connection error: {str(e)}"
