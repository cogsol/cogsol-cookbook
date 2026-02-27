from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.searches import SemanticSearch


class SemanticSearchAgent(BaseAgent):
    system_prompt = Prompts.load("semanticsearch.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [SemanticSearch()]

    initial_message = (
        "Hello! I can help you find information in the knowledge base. "
        "Describe what you are looking for and I will search for you."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I could not find relevant results for that query. "
        "Try rephrasing your request or using different keywords."
    )

    class Meta:
        name = "SemanticSearchAgent"
        chat_name = "Semantic Search Assistant"
