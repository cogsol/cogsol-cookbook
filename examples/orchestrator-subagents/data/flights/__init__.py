from cogsol.content import BaseTopic


class FlightsTopic(BaseTopic):
    name = "flights"

    class Meta:
        description = "Flight routes, schedules, and pricing information"
