from cogsol.tools import BaseRetrievalTool

from data.retrievals import EuropeRetrieval, AsiaRetrieval, AmericasRetrieval


class EuropeSearch(BaseRetrievalTool):
    description = "Search travel destinations in Europe."
    retrieval = EuropeRetrieval
    parameters = []


class AsiaSearch(BaseRetrievalTool):
    description = "Search travel destinations in Asia."
    retrieval = AsiaRetrieval
    parameters = []


class AmericasSearch(BaseRetrievalTool):
    description = "Search travel destinations in the Americas."
    retrieval = AmericasRetrieval
    parameters = []
