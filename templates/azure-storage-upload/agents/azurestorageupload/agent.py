from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.tools import UploadToAzureStorage


class AzureStorageUploadAgent(BaseAgent):
    system_prompt = Prompts.load("azurestorageupload.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        UploadToAzureStorage(),
    ]

    initial_message = (
        "Hello! I can help you generate text documents and upload them "
        "to Azure Blob Storage. Tell me what document you need and "
        "I will create it and save it for you."
    )
    forced_termination_message = (
        "Thank you for using the Document Upload Assistant. "
        "Visit https://docs.cogsol.ai for the full reference."
    )
    no_information_message = (
        "I could not process that request. "
        "Try describing the document you would like to generate and upload."
    )

    class Meta:
        name = "AzureStorageUploadAgent"
        chat_name = "Document Upload Assistant"
