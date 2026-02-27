from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.tools import CallExternalApi


class ExternalApiAgent(BaseAgent):
    system_prompt = Prompts.load("externalapi.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        CallExternalApi(),
    ]

    initial_message = (
        "Hello! I can help you retrieve information from an external API. "
        "Ask me a question and I will query the API for you."
    )
    forced_termination_message = (
        "Thank you for using the assistant. "
        "For more information, visit https://docs.cogsol.ai."
    )
    no_information_message = (
        "I could not retrieve the information you need right now. "
        "Please try rephrasing your question or visit https://docs.cogsol.ai for help."
    )

    class Meta:
        name = "ExternalApiAgent"
        chat_name = "External API Assistant"
