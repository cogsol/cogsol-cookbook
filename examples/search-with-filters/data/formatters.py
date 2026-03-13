from cogsol.content import BaseReferenceFormatter


class MovieFormatter(BaseReferenceFormatter):
    name = "movie_formatter"
    description = "Reference format for movie documents."
    expression = "[{name}]"
