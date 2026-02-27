from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.tools import QueryExcelAttachment


class ExcelQueryAgent(BaseAgent):
    system_prompt = Prompts.load("excelquery.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        QueryExcelAttachment(),
    ]

    initial_message = (
        "Hello! I can help you analyze Excel spreadsheets. "
        "Upload an Excel file and ask me anything about the data."
    )
    forced_termination_message = (
        "Thank you for using the Excel Query Assistant. "
        "Visit https://docs.cogsol.ai for the full reference."
    )
    no_information_message = (
        "I could not process that request. "
        "Try uploading an Excel file and asking a question about its content."
    )

    class Meta:
        name = "ExcelQueryAgent"
        chat_name = "Excel Query Assistant"
