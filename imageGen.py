import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("KEY")

def imagine(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="1024x1024"
    )
    return response['data'][0]['url']