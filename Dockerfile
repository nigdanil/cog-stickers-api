FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip git curl && apt-get clean
RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install --timeout=300 -r requirements.txt

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
