from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.searches import FlightSearch


class FlightSearchAgent(BaseAgent):
    system_prompt = Prompts.load("flightsearch.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        FlightSearch(),
    ]

    initial_message = (
        "Hello! I can help you find flights. "
        "Tell me your origin, destination, and travel dates."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I could not find flights matching your criteria. "
        "Please visit https://docs.cogsol.ai for additional resources."
    )

    class Meta:
        name = "FlightSearchAgent"
        chat_name = "Flight Search Assistant"
