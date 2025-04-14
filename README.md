# Cog Stickers API

🚀 Генерация стикеров на основе текста с использованием Stable Diffusion.

## Установка и запуск

```bash
docker compose up --build
```

## Эндпоинты

- `POST /generate` — принимает JSON:
```json
{
  "text": "cute cat astronaut"
}
```

## Ответ
```json
{
  "status": "ok",
  "file": "output.png"
}
```

## Используемая модель

- `stabilityai/stable-diffusion-2-1`
