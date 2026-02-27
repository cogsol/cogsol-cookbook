from cogsol.content import BaseRetrieval, ReorderingStrategy

from data.flights import FlightsTopic
from data.hotels import HotelsTopic
from data.policies import PoliciesTopic
from data.formatters import TravelFormatter


class FlightsRetrieval(BaseRetrieval):
    name = "orchestrator_flights"
    topic = FlightsTopic

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


class HotelsRetrieval(BaseRetrieval):
    name = "orchestrator_hotels"
    topic = HotelsTopic

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


class PoliciesRetrieval(BaseRetrieval):
    name = "orchestrator_policies"
    topic = PoliciesTopic

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
