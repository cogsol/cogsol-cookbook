from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.tools import QuerySharePointExcel


class SharePointExcelAgent(BaseAgent):
    system_prompt = Prompts.load("sharepointexcel.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        QuerySharePointExcel(),
    ]

    initial_message = (
        "Hello! I can help you query data from Excel files stored in "
        "SharePoint. Tell me which file, worksheet, and range you need "
        "and I will retrieve the data for you."
    )
    forced_termination_message = (
        "Thank you for using the SharePoint Excel Assistant. "
        "Visit https://docs.cogsol.ai for the full reference."
    )
    no_information_message = (
        "I could not process that request. "
        "Try specifying the Excel file name, worksheet, and cell range."
    )

    class Meta:
        name = "SharePointExcelAgent"
        chat_name = "SharePoint Excel Assistant"
