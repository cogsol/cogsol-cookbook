from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from agents.searches import MovieSearch


class MovieSearchAgent(BaseAgent):
    system_prompt = Prompts.load("moviesearch.md")
    generation_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    tools = [MovieSearch()]

    initial_message = (
        "Hello! I am the Movie Search Assistant. "
        "I can help you find movies by describing what you are looking for. "
        "You can also narrow results by genre, language, or decade. "
        "Try asking me something like 'a suspenseful movie set in space' "
        "or 'a French comedy from the 2000s'."
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I could not find a matching movie for that query. "
        "Try rephrasing your request or adjusting the filters."
    )

    class Meta:
        name = "MovieSearchAgent"
        chat_name = "Movie Search Assistant"
