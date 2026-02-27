from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts


class SpecialistBAgent(BaseAgent):
    system_prompt = Prompts.load("specialistb.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = []

    initial_message = (
        "Hello! I am Specialist B. "
        "Ask me anything within my area of expertise."
    )
    forced_termination_message = (
        "Thank you for using the assistant. "
        "For more information, visit https://docs.cogsol.ai."
    )
    no_information_message = (
        "I could not find the information you need right now. "
        "Please visit https://docs.cogsol.ai for additional resources."
    )

    class Meta:
        name = "SpecialistBAgent"
        chat_name = "Specialist B"
