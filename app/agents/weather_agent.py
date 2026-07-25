from app.tools.weather_tool import get_weather
from app.prompts.weather_prompt import WEATHER_PROMPT
from app.utils.llm import llm


def weather_agent(state):

    city = state["user_input"].split("to")[-1].strip()

    weather = get_weather(city)

    prompt = WEATHER_PROMPT.format(
        plan=state["plan"],
        weather=weather,
    )

    answer = llm.invoke(prompt)

    state["weather"] = answer

    return state