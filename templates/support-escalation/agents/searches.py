from cogsol.tools import BaseRetrievalTool

from data.retrievals import EscalationRetrieval


class EscalationSearch(BaseRetrievalTool):
    description = "Search the knowledge base for guides, policies, and how-to articles."
    retrieval = EscalationRetrieval
    parameters = []
