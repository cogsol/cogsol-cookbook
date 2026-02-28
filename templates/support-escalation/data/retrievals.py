from cogsol.content import BaseRetrieval, ReorderingStrategy

from data.knowledgebase import KnowledgeBaseTopic
from data.formatters import EscalationFormatter


class EscalationRetrieval(BaseRetrieval):
    name = "escalation_search"
    topic = KnowledgeBaseTopic

    num_refs = 5
    max_msg_length = 570

    reordering = False
    strategy_reordering = ReorderingStrategy.NONE

    previous_blocks = 1
    next_blocks = 1

    contingency_for_embedding = True
    threshold_similarity = 0.70

    formatters = {
        "Markdown": EscalationFormatter,
    }
    filters = []
