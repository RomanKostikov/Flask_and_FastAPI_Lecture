# Автоматическая документация по API
# FastAPI обладает встроенным инструментом для автоматической документации
# API, который позволяет быстро и удобно ознакомиться с функциональностью
# приложения. Рассмотрим два варианта документации API: интерактивную
# документацию Swagger и альтернативную документацию ReDoc.
# Интерактивная документация Swagger
# Swagger — это инструмент для создания и документирования API. FastAPI
# использует Swagger UI для генерации интерактивной документации, которая
# отображает все маршруты, параметры и модели данных, которые были определены
# в приложении.
# Пример использования
# Для того чтобы включить генерацию документации API в FastAPI, нужно
# использовать модуль fastapi.openapi. Например, вот как выглядит простой пример
# приложения с одним маршрутом:
import logging
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def root():
    logger.info('Отработал GET запрос.')
    return {"message": "Hello World"}


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id ={item_id}.')
    return {"item_id": item_id}
# app.openapi = custom_openapi
# В этом примере мы переопределили метод custom_openapi, который генерирует
# схему OpenAPI вручную. Мы также установили значение параметра openapi_url,
# чтобы FastAPI знал, где разместить схему OpenAPI.
# После запуска приложения можно перейти по адресу
# http://localhost:8000/api/v1/openapi.json и убедиться, что схема OpenAPI была
# успешно сгенерирована.
# Затем можно запустить приложение и перейти по адресу http://localhost:8000/docs
# или http://localhost:8000/redoc, чтобы просмотреть сгенерированную
# документацию.
