from cogsol.tools import BaseRetrievalTool

from data.retrievals import RecipeRetrieval


class RecipeSearch(BaseRetrievalTool):
    description = "Search recipes by ingredients, cuisine, dish type, or any food-related query."
    retrieval = RecipeRetrieval
    parameters = []
