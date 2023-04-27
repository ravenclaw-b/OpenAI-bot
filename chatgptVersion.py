import openai
import os 
import discord
import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("KEY")

# Initialize Discord client with all intents
client = discord.Client(intents=discord.Intents.all())

# Get start time for logging
startTime = str(datetime.datetime.now()).split(".")[0]

# Initialize context with system message
context = [
          {"role": "system", "content": "You are a helpful assistant!"}
      ]

# Open file for logging messages
fhandle = open(f"data/textlogs/log: {startTime}.txt", "a")

# Write start time to log file
fhandle.write(f"Bot started at {startTime} \n \n \n")

# Function to generate response using OpenAI GPT-3 model
def gpt(messages, prompt):
  context = messages
  context.append({"role": "user", "content": prompt})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=context
  )

  # Print response to console and write to log file
  print(f"User: {prompt} \nBot: {response['choices'][0]['message']['content']} \n")
  fhandle.write(f"User: {prompt} \nBot: {response['choices'][0]['message']['content']} \n")

  context.append(response['choices'][0]['message'])
  return context

# Event handler for when Discord client is ready
@client.event
async def on_ready():
   print("Bot is ready. \n")

# Event handler for when a message is received
@client.event
async def on_message(message):
   msg = message.content
   if msg.startswith("!gpt"):
       # Generate response using GPT-3 and send it to the channel
       await message.channel.send(gpt(context, msg.split("!gpt")[1])[-1]["content"])

# Start Discord client with token from environment variable
client.run(os.getenv("TOKEN"))
