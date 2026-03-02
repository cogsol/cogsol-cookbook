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
        "Hello! I am the Pretools Assistant. "
        "Before each response, three pretools run automatically: "
        "one fetches the current date and time, another checks "
        "the weather in Montevideo, and a third picks a daily CogSol tip. "
        "Ask me anything and you will see them in action!"
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I don't have specific information about that topic. "
        "Please check the official documentation at https://docs.cogsol.ai."
    )

    class Meta:
        name = "PretoolsAgent"
        chat_name = "Pretools Assistant"
