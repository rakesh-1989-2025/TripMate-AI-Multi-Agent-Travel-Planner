from app.graph.workflow import graph


def run_trip(user_input):

    state = {
        "user_input": user_input,
        "plan": "",
        "weather": "",
        "places": "",
        "flights": "",
        "hotels": "",
        "budget": "",
        "itinerary": "",
        "final_plan": "",
    }

    return graph.invoke(state)