from cogsol.content import BaseReferenceFormatter


class HelpDeskFormatter(BaseReferenceFormatter):
    name = "helpdesk_formatter"
    description = "Reference format for IT knowledge base articles."
    expression = "[{name}]"
