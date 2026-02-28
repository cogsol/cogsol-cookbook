from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.searches import EscalationSearch
from agents.tools import CreateTicket


class SupportEscalationAgent(BaseAgent):
    system_prompt = Prompts.load("supportescalation.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        EscalationSearch(),
        CreateTicket(),
    ]

    initial_message = (
        "Hello! I am the Support Escalation Assistant. "
        "I can search the knowledge base for answers and create "
        "support tickets when needed. How can I help you?"
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I could not find information about that topic. "
        "Would you like me to create a support ticket so a team member "
        "can assist you?"
    )

    class Meta:
        name = "SupportEscalationAgent"
        chat_name = "Support Escalation Assistant"
