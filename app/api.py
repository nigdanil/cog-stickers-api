from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from diffusers import StableDiffusionPipeline
import torch
import uuid
from pathlib import Path

app = FastAPI()

pipeline = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float16,
    revision="fp16"
)
pipeline = pipeline.to("cuda")

class GenerateRequest(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = ""
    width: int = 768
    height: int = 768
    steps: int = 20
    guidance_scale: float = 7.5
    seed: Optional[int] = None
    style: Optional[str] = "kawaii"
    output_format: str = "webp"
    output_quality: int = 90

@app.post("/generate")
def generate(req: GenerateRequest):
    try:
        generator = torch.manual_seed(req.seed) if req.seed is not None else None
        final_prompt = f"{req.style}, {req.prompt}" if req.style else req.prompt
        image = pipeline(
            prompt=final_prompt,
            negative_prompt=req.negative_prompt,
            height=req.height,
            width=req.width,
            num_inference_steps=req.steps,
            guidance_scale=req.guidance_scale,
            generator=generator
        ).images[0]

        Path("outputs").mkdir(exist_ok=True)
        filename = f"outputs/image-{uuid.uuid4().hex[:8]}.{req.output_format}"
        image.save(filename, format=req.output_format.upper(), quality=req.output_quality)
        return {"image_path": f"/{filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
