import os
import torch
torch.cuda.empty_cache()
from diffusers import StableDiffusionPipeline 

SDV5_MODEL_PATH = r"C:\Users\bamdad\stable-diffusion-v1-5"
SAVE_PATH = os.path.join(os.environ["USERPROFILE"], "Desktop", "SD_OUTPUT")

if not os.path.exists:
    os.mkdir(SAVE_PATH)

def uniquify(path):
    filename, extention = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extention
        counter += 1
        
    return path

prompt = "person"

pipe = StableDiffusionPipeline.from_pretrained(SDV5_MODEL_PATH)
pipe = pipe.to("cuda")

with torch.autocast("cuda"):
    image = pipe(prompt).images[0]

image_path = uniquify(os.path.join(SAVE_PATH, (prompt[::25] + "...") if len(prompt) > 25 else prompt) + ".png")
print(image_path)

image.save(image_path) 