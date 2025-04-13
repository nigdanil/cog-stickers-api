
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip git curl && apt-get clean
RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install --timeout=300 -r requirements.txt
RUN pip install --timeout=300 git+https://github.com/replicate/cog.git

ENV PATH="/root/.local/bin:$PATH"
ENV COG_PREDICT_MODULE=predict

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
