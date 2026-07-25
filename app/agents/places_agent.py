from app.prompts.places_prompt import PLACES_PROMPT
from app.utils.llm import llm


def places_agent(state):

    prompt = PLACES_PROMPT.format(
        plan=state["plan"]
    )

    result = llm.invoke(prompt)

    state["places"] = result

    return state