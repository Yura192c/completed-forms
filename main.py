from fastapi import FastAPI
from routes.route import router

app = FastAPI(title="API для определения заполненных форм.",
              description="Тестовое задание e.Kom")

app.include_router(router)
