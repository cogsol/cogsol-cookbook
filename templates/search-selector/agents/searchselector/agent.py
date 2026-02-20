from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.tools import SearchInformation
from agents.searches import EuropeSearch, AsiaSearch, AmericasSearch


class SearchSelectorAgent(BaseAgent):
    system_prompt = Prompts.load("searchselector.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [
        SearchInformation(),
        EuropeSearch(),
        AsiaSearch(),
        AmericasSearch(),
    ]

    initial_message = (
        "Hello! I am the Travel Guide Assistant. "
        "I can help you find information about destinations in Europe, Asia, "
        "and the Americas. Ask me about attractions, local cuisine, "
        "best times to visit, or travel tips for any destination."
    )
    forced_termination_message = (
        "Thank you for using the Travel Guide Assistant. "
        "Visit https://docs.cogsol.ai for the full reference."
    )
    no_information_message = (
        "I could not find information matching that query. "
        "Try asking about a specific destination or region."
    )

    class Meta:
        name = "SearchSelectorAgent"
        chat_name = "Travel Guide Assistant"
