
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import subprocess

app = FastAPI()

class GenerateRequest(BaseModel):
    prompt: str
    style: str = "kawaii"
    width: int = 1152
    height: int = 1152
    steps: int = 17
    seed: Optional[int] = None
    output_format: str = "webp"
    output_quality: int = 90
    negative_prompt: str = ""
    number_of_images: int = 1

@app.post("/generate")
def generate(req: GenerateRequest):
    try:
        args = [
            "cog", "predict",
            "-i", f"prompt={req.prompt}",
            "-i", f"style={req.style}",
            "-i", f"width={req.width}",
            "-i", f"height={req.height}",
            "-i", f"steps={req.steps}",
            "-i", f"output_format={req.output_format}",
            "-i", f"output_quality={req.output_quality}",
            "-i", f"negative_prompt={req.negative_prompt}",
            "-i", f"number_of_images={req.number_of_images}"
        ]
        if req.seed is not None:
            args += ["-i", f"seed={req.seed}"]
        result = subprocess.run(args, capture_output=True, text=True)
        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=result.stderr)
        return {"output": result.stdout.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
