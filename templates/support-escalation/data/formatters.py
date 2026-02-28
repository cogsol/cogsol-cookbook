from cogsol.content import BaseReferenceFormatter


class EscalationFormatter(BaseReferenceFormatter):
    name = "escalation_formatter"
    description = "Reference format for knowledge base articles."
    expression = "[{name}]"
