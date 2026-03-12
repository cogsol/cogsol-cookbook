from cogsol.tools import BaseRetrievalTool

from data.retrievals import HelpDeskRetrieval


class HelpDeskSearch(BaseRetrievalTool):
    description = "Search the IT knowledge base for troubleshooting guides, policies, and how-to articles."
    retrieval = HelpDeskRetrieval
    parameters = []
