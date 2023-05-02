import openai
import os
from dotenv import load_dotenv
import datetime
import requests
from io import BytesIO

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("KEY")

def imagine(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    # Retrieve binary data from response
    image_data = requests.get(response['data'][0]['url']).content

    # Save image data as PNG file
    file_path = f"data/pictures/{str(datetime.datetime.now()).split('.')[0]}.png"
    with open(file_path, 'wb') as f:
        f.write(image_data)

    return response['data'][0]['url']