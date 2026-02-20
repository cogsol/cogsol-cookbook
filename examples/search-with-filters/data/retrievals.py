from cogsol.content import BaseRetrieval, ReorderingStrategy

from data.movies import MoviesTopic
from data.movies.metadata import GenreMetadata, LanguageMetadata, DecadeMetadata
from data.formatters import MovieFormatter


class MovieRetrieval(BaseRetrieval):
    name = "movie_search"
    topic = MoviesTopic

    num_refs = 5
    max_msg_length = 570

    reordering = False
    strategy_reordering = ReorderingStrategy.NONE

    previous_blocks = 1
    next_blocks = 1

    contingency_for_embedding = True
    threshold_similarity = 0.70

    formatters = {
        "Markdown": MovieFormatter,
    }
    filters = [GenreMetadata, LanguageMetadata, DecadeMetadata]
