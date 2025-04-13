
# 🧠 Cog Stickers API

### 📦 Что это?
Контейнеризованный FastAPI-сервер для генерации изображений с помощью моделей diffusers + Cog.

### 🚀 Как использовать (локально)

```bash
docker build -t cog-stickers .
docker run --rm -p 8000:8000 cog-stickers
```

### ⚙️ CI/CD + Яндекс Облако

1. Добавь `.github/workflows/docker.yml`
2. В настройках репозитория GitHub добавь Secrets:
   - `YC_OAUTH_TOKEN`
   - `YC_REGISTRY_ID`

3. После пуша в `main` — GitHub сам соберёт и зальёт образ в Яндекс Контейнерный Реестр.

### ☁️ Развёртывание

```bash
yc serverless container create   --name=cog-api   --folder-id=<folder-id>   --image=cr.yandex/<registry-id>/cog-stickers:latest   --memory=4G   --cores=2   --port=8000
```

Enjoy 😎
