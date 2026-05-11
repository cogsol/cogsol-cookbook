from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.tools import QueryExcelAttachment


class ExpenseReviewAgent(BaseAgent):
    system_prompt = Prompts.load("expensereview.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        QueryExcelAttachment(),
    ]

    initial_message = (
        "Hello! I am the Expense Review Assistant. "
        "Upload an expense report (.xlsx) and I can help you review it: "
        "totals by category, expenses by employee, pending approvals, and more."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I could not process that request. "
        "Please upload an Excel expense report and ask a question about it."
    )

    class Meta:
        name = "ExpenseReviewAgent"
        chat_name = "Expense Review Assistant"
