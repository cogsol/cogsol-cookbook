from cogsol.content import BaseTopic


class DocumentsTopic(BaseTopic):
    name = "documents"

    class Meta:
        description = "Document collection for semantic search"
