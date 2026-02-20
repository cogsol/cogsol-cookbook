from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.searches import RecipeSearch


class RecipeSearchAgent(BaseAgent):
    system_prompt = Prompts.load("recipesearch.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [RecipeSearch()]

    initial_message = (
        "Hello! I am the Recipe Search Assistant. "
        "I can help you find recipes by ingredients, cuisine type, "
        "or any description of what you are in the mood for. "
        "Try asking me something like 'something light with chicken' "
        "or 'an easy chocolate dessert'."
    )
    forced_termination_message = (
        "Thank you for using the Recipe Search Assistant. "
        "Visit https://docs.cogsol.ai for the full reference."
    )
    no_information_message = (
        "I could not find a matching recipe for that query. "
        "Try rephrasing your request or using different keywords."
    )

    class Meta:
        name = "RecipeSearchAgent"
        chat_name = "Recipe Search Assistant"
