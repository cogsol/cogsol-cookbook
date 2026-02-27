from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts


class LessonsDocsAgent(BaseAgent):
    system_prompt = Prompts.load("lessons.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    initial_message = (
        "Hello! I am the Lessons Docs Assistant. "
        "Ask me about the CogSol platform: assistant configuration, "
        "tools and searches, content management, troubleshooting, "
        "or evaluation and improvement."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I don't have specific information about that topic. "
        "Please check the official documentation at https://docs.cogsol.ai."
    )

    class Meta:
        name = "LessonsDocsAgent"
        chat_name = "Lessons Docs Assistant"
