from cogsol.content import BaseRetrieval, ReorderingStrategy

from data.recipes import RecipesTopic
from data.formatters import RecipeFormatter


class RecipeRetrieval(BaseRetrieval):
    name = "recipe_search"
    topic = RecipesTopic

    num_refs = 5
    max_msg_length = 1800

    reordering = False
    strategy_reordering = ReorderingStrategy.NONE

    previous_blocks = 1
    next_blocks = 1

    contingency_for_embedding = True
    threshold_similarity = 0.70

    formatters = {
        "Markdown": RecipeFormatter,
    }
    filters = []
