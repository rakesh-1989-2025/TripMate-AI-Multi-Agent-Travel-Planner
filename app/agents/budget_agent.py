from app.prompts.budget_prompt import BUDGET_PROMPT
from app.utils.llm import llm


def budget_agent(state):

    prompt = BUDGET_PROMPT.format(
        plan=state["plan"],
        flights=state["flights"],
        hotels=state["hotels"],
    )

    result = llm.invoke(prompt)

    state["budget"] = result

    return state