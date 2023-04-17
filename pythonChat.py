import openai
import os 

from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("KEY")

openai.api_key = KEY


context = [
          {"role": "system", "content": "You are a 10 year old boy"}
      ]

def gpt(messages, prompt):
  context = messages
  context.append({"role": "user", "content": prompt})
  response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=context
  )

  context.append(response['choices'][0]['message'])

  return context

while True:
    prompt = input("You: ")
    context = gpt(context, prompt)
    print("Bot: " + context[-1]["content"])

