import openai
import os 
import discord

from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("KEY")

openai.api_key = KEY

client = discord.Client(intents=discord.Intents.all())

prompt=""

def davinci(prompt):
   response =  openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
   with open("logs.txt", "a") as f:
      f.write(str(response))
   return response["choices"][0]["text"]

@client.event
async def on_ready():
   print("hi")

@client.event
async def on_message(message):
   msg = message.content
   if msg.startswith("!davinci"):
      await message.channel.send(davinci(msg.split("!davinci")[1]))

client.run(os.getenv("TOKEN"))