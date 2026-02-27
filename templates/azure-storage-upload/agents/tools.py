from cogsol.tools import BaseTool, tool_params


class UploadToAzureStorage(BaseTool):
    """Script tool that uploads a text document to Azure Blob Storage."""

    name = "upload_to_azure_storage"
    description = (
        "Upload a text document to Azure Blob Storage. "
        "Use this to save generated content as a file in the cloud."
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
                "Name for the file in storage, including extension "
                "(e.g. report.txt, summary.md)."
            ),
            "type": "string",
            "required": True,
        },
    )
    def run(self, content="", filename="", chat=None, data=None, secrets=None, log=None):
        from urllib import request, error

        account = secrets.get("AZURE_STORAGE_ACCOUNT", "")
        container = secrets.get("AZURE_CONTAINER_NAME", "")
        sas_token = secrets.get("AZURE_SAS_TOKEN", "")

        if not all([account, container, sas_token]):
            return "Missing Azure Storage configuration. Check platform secrets."

        url = (
            f"https://{account}.blob.core.windows.net"
            f"/{container}/{filename}?{sas_token}"
        )

        headers = {
            "x-ms-blob-type": "BlockBlob",
            "Content-Type": "text/plain; charset=utf-8",
            "x-ms-version": "2021-06-08",
        }

        req = request.Request(
            url, data=content.encode("utf-8"), headers=headers, method="PUT"
        )

        try:
            with request.urlopen(req) as resp:
                log.append(f"Upload successful: {resp.status}")
                blob_url = (
                    f"https://{account}.blob.core.windows.net"
                    f"/{container}/{filename}"
                )
                return f"Document uploaded successfully.\n\nBlob URL: {blob_url}"
        except error.HTTPError as e:
            log.append(f"Upload failed: {e.code} {e.reason}")
            return f"Upload failed: {e.code} {e.reason}"
        except error.URLError as e:
            log.append(f"Connection error: {str(e)}")
            return f"Connection error: {str(e)}"
