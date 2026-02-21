from cogsol.content import BaseTopic


class MoviesTopic(BaseTopic):
    name = "movies"

    class Meta:
        description = "Collection of movie synopses for semantic search with filters"
