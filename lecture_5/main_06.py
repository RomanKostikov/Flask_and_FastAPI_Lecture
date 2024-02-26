# Основы протокола HTTP
# Обработка запросов DELETE
# Метод DELETE используется для удаления данных на сервере. В FastAPI обработка
# DELETE-запросов происходит с помощью декоратора @app.delete(). Например:
import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id ={item_id}.')
    return {"item_id": item_id}
# Этот код создает приложение FastAPI и добавляет обработчик DELETE-запросов для
# URL-адреса /items/{item_id}. Функция delete_item() принимает идентификатор
# элемента и возвращает JSON-объект с этим идентификатором.
# 🔥 Важно! Зачастую операция удаления не удаляет данные из базы данных, а
# изменяет специально созданное поле is_deleted на значение Истина. Таким
# образов вы сможете восстановить ранее удалённные данные
# пользователя, если он передумает спустя время.
