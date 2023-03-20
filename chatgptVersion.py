import openai
import os 
import discord

from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("KEY")

openai.api_key = KEY

client = discord.Client(intents=discord.Intents.all())

context = [
          {"role": "system", "content": "You are a helpful assistant!"}
      ]

def gpt(messages, prompt):
  context = messages
  context.append({"role": "user", "content": prompt})
  response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=context
  )

  context.append(response['choices'][0]['message'])

  print(context[-1]["content"])
  return context

@client.event
async def on_ready():
   print("hi")

@client.event
async def on_message(message):
   msg = message.content
   if msg.startswith("!gpt"):
       #await message.channel.send(
       gpt(context, msg.split("!gpt")[1])[-1]["content"]
       print(gpt(context, msg.split("!gpt")[1]))

client.run(os.getenv("TOKEN"))