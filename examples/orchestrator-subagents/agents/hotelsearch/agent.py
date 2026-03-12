from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.searches import HotelSearch


class HotelSearchAgent(BaseAgent):
    system_prompt = Prompts.load("hotelsearch.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        HotelSearch(),
    ]

    initial_message = (
        "Hello! I can help you find hotels. "
        "Tell me the city, area, and your travel dates."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I could not find hotels matching your criteria. "
        "Please visit https://docs.cogsol.ai for additional resources."
    )

    class Meta:
        name = "HotelSearchAgent"
        chat_name = "Hotel Search Assistant"
