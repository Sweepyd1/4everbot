import requests
from environs import Env

env = Env()
env.read_env()

CATALOG_ID = env.str("CATALOG_ID")
SECRET_KEY = env.str("SECRET_KEY")


prompt = {
    "modelUri": f"gpt://{CATALOG_ID}/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "user",
            "text": "Привет! Как у тебя дела? Какая ты языковая модель?"
        }
    ]
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {SECRET_KEY}"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(result)
