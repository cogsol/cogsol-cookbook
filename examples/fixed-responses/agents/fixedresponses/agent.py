from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts


class FixedResponsesDocsAgent(BaseAgent):
    system_prompt = Prompts.load("fixedresponses.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    initial_message = (
        "Hello! I am the Fixed Responses Docs Assistant. "
        "Ask me about installation, setup, agents, migrations, "
        "or any other topic covered in the CogSol Framework documentation."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I don't have specific information about that topic. "
        "Please check the official documentation at https://docs.cogsol.ai."
    )

    class Meta:
        name = "FixedResponsesDocsAgent"
        chat_name = "Fixed Responses Docs Assistant"
