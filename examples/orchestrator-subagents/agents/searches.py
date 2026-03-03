from cogsol.tools import BaseRetrievalTool

from data.retrievals import FlightsRetrieval, HotelsRetrieval, PoliciesRetrieval


class FlightSearch(BaseRetrievalTool):
    description = "Search available flight routes, schedules, and pricing."
    retrieval = FlightsRetrieval
    parameters = []


class HotelSearch(BaseRetrievalTool):
    description = "Search hotel accommodations, locations, and rates."
    retrieval = HotelsRetrieval
    parameters = []


class PolicySearch(BaseRetrievalTool):
    description = "Search corporate travel expense policies and approval rules."
    retrieval = PoliciesRetrieval
    parameters = []
