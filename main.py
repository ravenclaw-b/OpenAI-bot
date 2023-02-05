import openai
import os 
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("KEY")

openai.api_key = KEY

prompt=""

response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=50)

print(response["choices"][0]["text"])