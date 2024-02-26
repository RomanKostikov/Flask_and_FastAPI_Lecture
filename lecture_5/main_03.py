# Основы протокола HTTP
# Обработка запросов GET
# Метод GET используется для получения ресурсов с сервера. В FastAPI обработка
# GET-запросов происходит с помощью декоратора @app.get(). Например:
import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "World"}
# Этот код создает приложение FastAPI и добавляет обработчик GET-запросов для
# корневого URL-адреса. Функция read_root() возвращает JSON-объект {"Hello":
# "World"}.
