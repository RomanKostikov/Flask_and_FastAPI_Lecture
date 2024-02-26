# Основы протокола HTTP
# Обработка запросов POST
# Метод POST используется для отправки данных на сервер. В FastAPI обработка
# POST-запросов происходит с помощью декоратора @app.post(). Например:
import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item
# Этот код создает приложение FastAPI и добавляет обработчик POST-запросов для
# URL-адреса /items/. Функция create_item() принимает объект Item и возвращает его же.
# 🔥 Внимание! Код выше не будет работать, так как мы не определили объект
# Item. Речь о модуле pydantic позволяющем создать класс Item будет позже
# в рамках курса.
