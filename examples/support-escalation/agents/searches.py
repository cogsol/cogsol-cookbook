from cogsol.tools import BaseRetrievalTool

from data.retrievals import HelpDeskRetrieval


class HelpDeskSearch(BaseRetrievalTool):
    description = "Search the IT knowledge base for troubleshooting guides, policies, and how-to articles. Optionally filter by category."
    retrieval = HelpDeskRetrieval
    parameters = [
        {
            "name": "question",
            "description": "Search query describing the issue or topic",
            "type": "string",
            "required": True,
        },
        {
            "name": "category",
            "description": "Filter by article category: Network, Hardware, Software, Security, or Onboarding",
            "type": "string",
            "required": False,
        },
    ]
