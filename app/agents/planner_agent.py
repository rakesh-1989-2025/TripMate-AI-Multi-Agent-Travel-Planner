from app.prompts.planner_prompt import PLANNER_PROMPT
from app.utils.llm import llm


def planner_agent(state):

    prompt = PLANNER_PROMPT.format(
        user_input=state["user_input"]
    )

    result = llm.invoke(prompt)

    state["plan"] = result

    return state