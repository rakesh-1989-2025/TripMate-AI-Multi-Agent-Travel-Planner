import requests

from app.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
    OPENROUTER_URL,
)


class OpenRouterLLM:

    def invoke(self, prompt: str):

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=60,
        )

        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        data = response.json()

        if response.status_code != 200:
            raise Exception(f"OpenRouter Error:\n{data}")

        if "choices" not in data:
            raise Exception(f"'choices' not found.\nResponse:\n{data}")

        return data["choices"][0]["message"]["content"]


llm = OpenRouterLLM()