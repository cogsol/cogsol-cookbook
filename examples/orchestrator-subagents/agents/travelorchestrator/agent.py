from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.tools import PlanTravel


class TravelOrchestratorAgent(BaseAgent):
    system_prompt = Prompts.load("travelorchestrator.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 1

    tools = [
        PlanTravel(),
    ]

    initial_message = (
        "Welcome! I can help you plan business trips. "
        "For example: \"I need to fly from Buenos Aires to Madrid next Monday, "
        "returning March 7. I'd like a hotel near Castellana.\""
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I could not find the information you need right now. "
        "Please visit https://docs.cogsol.ai for additional resources."
    )

    class Meta:
        name = "TravelOrchestratorAgent"
        chat_name = "Corporate Travel Assistant"
