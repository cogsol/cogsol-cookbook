from cogsol.content import BaseRetrieval, ReorderingStrategy

from data.europe import EuropeTopic
from data.asia import AsiaTopic
from data.americas import AmericasTopic
from data.formatters import TravelFormatter


class EuropeRetrieval(BaseRetrieval):
    name = "search_selector_europe"
    topic = EuropeTopic

    num_refs = 5
    max_msg_length = 570

    reordering = False
    strategy_reordering = ReorderingStrategy.NONE

    previous_blocks = 1
    next_blocks = 1

    contingency_for_embedding = True
    threshold_similarity = 0.70

    formatters = {
        "Markdown": TravelFormatter,
    }
    filters = []


class AsiaRetrieval(BaseRetrieval):
    name = "search_selector_asia"
    topic = AsiaTopic

    num_refs = 5
    max_msg_length = 570

    reordering = False
    strategy_reordering = ReorderingStrategy.NONE

    previous_blocks = 1
    next_blocks = 1

    contingency_for_embedding = True
    threshold_similarity = 0.70

    formatters = {
        "Markdown": TravelFormatter,
    }
    filters = []


class AmericasRetrieval(BaseRetrieval):
    name = "search_selector_americas"
    topic = AmericasTopic

    num_refs = 5
    max_msg_length = 570

    reordering = False
    strategy_reordering = ReorderingStrategy.NONE

    previous_blocks = 1
    next_blocks = 1

    contingency_for_embedding = True
    threshold_similarity = 0.70

    formatters = {
        "Markdown": TravelFormatter,
    }
    filters = []
