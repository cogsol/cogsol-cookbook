from cogsol.content import BaseReferenceFormatter


class TravelFormatter(BaseReferenceFormatter):
    name = "orchestrator_formatter"
    description = "Reference format for travel planning documents."
    expression = "[{name}]"
