# Введение в FastAPI и его возможности
# Настройка сервера и маршрутизации
# Далее необходимо настроить сервер и определить маршрутизацию для нашего
# приложения. Для этого создайте функции-обработчики запросов и определите их
# маршруты.
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
# В этом примере мы определили две функции-обработчика запросов. Первая
# функция обрабатывает GET-запрос по корневому пути "/" и возвращает словарь с
# сообщением "Hello World". Вторая функция обрабатывает GET-запрос по пути
# "/items/{item_id}", где item_id — это переменная пути, а q — это параметр запроса.
# Функция возвращает словарь с переданными параметрами.
# Запуск приложения и проверка работоспособности
# Для запуска приложения необходимо использовать сервер для запуска приложений
# uvicorn. Для этого выполните следующую команду:
# uvicorn main:app --reload
# Эта команда запустит сервер на локальном хосте по адресу http://127.0.0.1:8000/.
# Чтобы проверить работоспособность приложения, откройте браузер и перейдите по
# адресу http://127.0.0.1:8000/. Вы должны увидеть сообщение "Hello World".
# Чтобы проверить работу второй функции, перейдите по адресу
# http://127.0.0.1:8000/items/5?q=test, где 5 — это значение переменной item_id, а
# test — значение параметра q. Вы должны увидеть словарь с переданными
# параметрами.