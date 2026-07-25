from app.prompts.itinerary_prompt import ITINERARY_PROMPT
from app.utils.llm import llm


def itinerary_agent(state):

    prompt = ITINERARY_PROMPT.format(
        plan=state["plan"],
        weather=state["weather"],
        places=state["places"],
        flights=state["flights"],
        hotels=state["hotels"],
        budget=state["budget"],
    )

    result = llm.invoke(prompt)

    state["itinerary"] = result

    return state