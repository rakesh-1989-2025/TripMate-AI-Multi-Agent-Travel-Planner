from app.prompts.flight_prompt import FLIGHT_PROMPT
from app.utils.llm import llm


def flight_agent(state):

    prompt = FLIGHT_PROMPT.format(
        plan=state["plan"]
    )

    answer = llm.invoke(prompt)

    state["flights"] = answer

    return state