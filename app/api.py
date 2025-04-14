from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
import torch

app = FastAPI()

class Prompt(BaseModel):
    text: str

pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float16
).to("cuda")

@app.post("/generate")
async def generate(prompt: Prompt):
    try:
        image = pipe(prompt.text).images[0]
        image.save("output.png")
        return {"status": "ok", "file": "output.png"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
