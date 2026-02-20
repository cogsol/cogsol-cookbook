from cogsol.tools import BaseRetrievalTool

from data.retrievals import DocumentRetrieval


class SemanticSearch(BaseRetrievalTool):
    description = "Semantic search over the document collection."
    retrieval = DocumentRetrieval
    parameters = []
