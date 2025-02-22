import openai
import time
from openai._exceptions import OpenAIError, RateLimitError

# Нужно получить API_KEY на https://platform.openai.com/
# Там нужно будет купить подписку. :(

MODEL_AI = "gpt-4o-mini"
client = openai.OpenAI(api_key="your_api_key")  # Directly passing API key


def ask_openai(question, retries=3, delay=5):
    """ Отправка запроса к OpenAI с обработкой ошибок и повтором. """
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_AI,
                messages=[{"role": "user", "content": question}],
                max_tokens=200
            )
            return response.choices[0].message.content

        except RateLimitError:
            print(f"Превышен лимит запросов! Повтор через {delay} секунд...")

        except OpenAIError as e:
            return f"Ошибка OpenAI: {e}"

        time.sleep(delay)  # Ждем перед повторной попыткой

    return "Не удалось получить ответ после нескольких попыток."


def test_func() -> None:

    mass = []

    try:
        # Заведомо обращаемся к несуществующему индексу
        print(f"Hello: {mass[1]}")

    except Exception as ex:
        print(ex)
        print(ask_openai(f"Ответь на русском: {ex}"))


if __name__ == "__main__":
    test_func()