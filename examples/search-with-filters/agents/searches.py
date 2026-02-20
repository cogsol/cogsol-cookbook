from cogsol.tools import BaseRetrievalTool

from data.retrievals import MovieRetrieval


class MovieSearch(BaseRetrievalTool):
    description = "Search movies by plot, theme, or any description. Optionally filter by genre, language, or decade."
    retrieval = MovieRetrieval
    parameters = [
        {
            "name": "question",
            "description": "Search query describing the movie",
            "type": "string",
            "required": True,
        },
        {
            "name": "genre",
            "description": "Filter by movie genre",
            "type": "string",
            "required": False,
        },
        {
            "name": "language",
            "description": "Filter by original language",
            "type": "string",
            "required": False,
        },
        {
            "name": "decade",
            "description": "Filter by decade of release",
            "type": "string",
            "required": False,
        },
    ]
