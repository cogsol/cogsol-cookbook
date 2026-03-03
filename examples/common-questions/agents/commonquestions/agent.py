from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts


class CommonQuestionsDocsAgent(BaseAgent):
    system_prompt = Prompts.load("commonquestions.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    initial_message = (
        "Hello! I am the Common Questions Docs Assistant. "
        "Ask me anything about what the CogSol Framework is, "
        "how its components work, or how they relate to each other."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I don't have specific information about that topic. "
        "Please check the official documentation at https://docs.cogsol.ai."
    )

    class Meta:
        name = "CommonQuestionsDocsAgent"
        chat_name = "Common Questions Docs Assistant"
