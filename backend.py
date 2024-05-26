import openai
from dotenv import load_dotenv
import os

load_dotenv(".env")

KEY = os.environ.get("API_KEY")


class Chatbot:
    def __init__(self):
        openai.api_key = KEY


    def get_response(self, user_input):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your are a helpful assistant"},
                {"role": "user", "content": user_input}
            ],
            max_tokens=3000,
            temperature=0.5
        ).choices[0].message.content
        return response



if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)

