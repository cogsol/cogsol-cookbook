from cogsol.content import BaseReferenceFormatter


class DocumentFormatter(BaseReferenceFormatter):
    name = "document_formatter"
    description = "Reference format for documents."
    expression = "[{name}]"
