from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.searches import PolicySearch


class ExpensePolicyAgent(BaseAgent):
    system_prompt = Prompts.load("expensepolicy.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        PolicySearch(),
    ]

    initial_message = (
        "Hello! I can help with corporate travel expense policies. "
        "Ask me about spending limits, approval workflows, or reporting requirements."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I could not find a policy matching your question. "
        "Please visit https://docs.cogsol.ai for additional resources."
    )

    class Meta:
        name = "ExpensePolicyAgent"
        chat_name = "Expense Policy Assistant"
