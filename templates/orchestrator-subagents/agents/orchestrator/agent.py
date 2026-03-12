from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.tools import ConsultSpecialists


class OrchestratorAgent(BaseAgent):
    system_prompt = Prompts.load("orchestrator.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 1

    tools = [
        ConsultSpecialists(),
    ]

    initial_message = (
        "Hello! I coordinate specialist agents to help you with your request. "
        "Describe what you need and I will consult the relevant specialists."
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
        name = "OrchestratorAgent"
        chat_name = "Orchestrator Assistant"
