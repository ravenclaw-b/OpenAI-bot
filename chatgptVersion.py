import os
import openai

from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("KEY")

openai.api_key = KEY

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a sarcastic 13 year old girl. A stereotypical gen z."},
        {"role": "user", "content": "Who won the world series in 2026?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response)