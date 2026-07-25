from app.prompts.hotel_prompt import HOTEL_PROMPT
from app.utils.llm import llm


def hotel_agent(state):

    prompt = HOTEL_PROMPT.format(
        plan=state["plan"]
    )

    answer = llm.invoke(prompt)

    state["hotels"] = answer

    return state