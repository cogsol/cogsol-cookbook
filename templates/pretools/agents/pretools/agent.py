from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from ..tools import CurrentDateTimeTool, WeatherInfoTool, DailyTipTool


class PretoolsAgent(BaseAgent):
    system_prompt = Prompts.load("pretools.md")
    generation_config = genconfigs.QA()
    pregeneration_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    pretools = [CurrentDateTimeTool(), WeatherInfoTool(), DailyTipTool()]

    initial_message = (
        "Hello! I am the Pretools Assistant. I use pre-processing tools "
        "to gather real-time context before responding. Ask me anything "
        "and I will include current date, weather, and a daily tip "
        "in my response."
    )
    forced_termination_message = (
        "Thank you for using the Pretools Assistant. "
        "Visit https://docs.cogsol.ai for the full reference."
    )
    no_information_message = (
        "I don't have specific information about that topic. "
        "Please check the official documentation at https://docs.cogsol.ai."
    )

    class Meta:
        name = "PretoolsAgent"
        chat_name = "Pretools Assistant"
