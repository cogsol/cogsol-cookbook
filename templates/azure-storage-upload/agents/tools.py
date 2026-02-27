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
        import io
        from datetime import datetime, timedelta, timezone
        from azure.storage.blob import (
            BlobServiceClient,
            generate_blob_sas,
            BlobSasPermissions,
            ContentSettings,
        )

        account_name = secrets.get("AZURE_ACCOUNT_NAME", "")
        account_key = secrets.get("AZURE_ACCOUNT_KEY", "")
        container_name = secrets.get("AZURE_CONTAINER_NAME", "")

        if not all([account_name, account_key, container_name]):
            return "Missing Azure Storage configuration. Check platform secrets."

        conn_str = (
            "DefaultEndpointsProtocol=https;"
            f"AccountName={account_name};"
            f"AccountKey={account_key};"
            "EndpointSuffix=core.windows.net"
        )

        try:
            svc = BlobServiceClient.from_connection_string(conn_str)
            blob_client = svc.get_blob_client(
                container=container_name, blob=filename
            )

            blob_client.upload_blob(
                io.BytesIO(content.encode("utf-8")),
                overwrite=True,
                content_settings=ContentSettings(
                    content_type="text/plain; charset=utf-8",
                ),
            )
            log.append(f"Upload successful: {filename}")

            sas_expiry = datetime.now(timezone.utc) + timedelta(minutes=60)
            sas_token = generate_blob_sas(
                account_name=account_name,
                account_key=account_key,
                container_name=container_name,
                blob_name=filename,
                permission=BlobSasPermissions(read=True),
                expiry=sas_expiry,
            )

            blob_url = (
                f"https://{account_name}.blob.core.windows.net"
                f"/{container_name}/{filename}?{sas_token}"
            )

            return (
                f"Document uploaded successfully.\n\n"
                f"Download URL (valid for 60 minutes):\n{blob_url}"
            )

        except Exception as e:
            log.append(f"Upload failed: {str(e)}")
            return f"Upload failed: {str(e)}"
