from cogsol.content import BaseReferenceFormatter


class TravelFormatter(BaseReferenceFormatter):
    name = "travel_formatter"
    description = "Reference format for travel destination documents."
    expression = "[{name}]"
