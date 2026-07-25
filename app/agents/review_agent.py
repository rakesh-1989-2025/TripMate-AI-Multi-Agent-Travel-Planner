from app.prompts.review_prompt import REVIEW_PROMPT
from app.utils.llm import llm


def review_agent(state):

    prompt = REVIEW_PROMPT.format(
        plan=state["plan"],
        weather=state["weather"],
        places=state["places"],
        flights=state["flights"],
        hotels=state["hotels"],
        budget=state["budget"],
        itinerary=state["itinerary"],
    )

    result = llm.invoke(prompt)

    state["final_plan"] = result

    return state