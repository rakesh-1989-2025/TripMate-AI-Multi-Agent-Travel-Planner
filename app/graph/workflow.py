from langgraph.graph import StateGraph, END

from app.graph.state import TripState

from app.agents.planner_agent import planner_agent
from app.agents.weather_agent import weather_agent
from app.agents.places_agent import places_agent
from app.agents.flight_agent import flight_agent
from app.agents.hotel_agent import hotel_agent
from app.agents.budget_agent import budget_agent
from app.agents.itinerary_agent import itinerary_agent
from app.agents.review_agent import review_agent

workflow = StateGraph(TripState)

workflow.add_node("planner", planner_agent)
workflow.add_node("weather", weather_agent)
workflow.add_node("places", places_agent)
workflow.add_node("flight", flight_agent)
workflow.add_node("hotel", hotel_agent)
workflow.add_node("budget", budget_agent)
workflow.add_node("itinerary", itinerary_agent)
workflow.add_node("review", review_agent)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "weather")
workflow.add_edge("weather", "places")
workflow.add_edge("places", "flight")
workflow.add_edge("flight", "hotel")
workflow.add_edge("hotel", "budget")
workflow.add_edge("budget", "itinerary")
workflow.add_edge("itinerary", "review")
workflow.add_edge("review", END)

graph = workflow.compile()