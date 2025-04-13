# 🚀 Cog Stickers API — Docker + GitHub Actions + Yandex Cloud

## 🔧 Setup

1. Добавь секреты в GitHub:
   - `YC_OAUTH_TOKEN`: [получи здесь](https://oauth.yandex.ru/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb)
   - `YC_REGISTRY_ID`: из Yandex Container Registry

2. Структура проекта:
```
.
├── Dockerfile
├── requirements.txt
├── api.py
└── .github/
    └── workflows/
        └── docker.yml
```

## 🚀 CI/CD

При `push` в `main`:
- собирается Docker-образ
- пушится в Yandex Container Registry