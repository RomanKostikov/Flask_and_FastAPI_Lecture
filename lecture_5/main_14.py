# Определение конечных точек API
# ● JSON объект
# В этом примере возвращается ответ JSON с настраиваемым сообщением и кодом
# состояния.
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)
# В этом примере мы импортируем класс JSONResponse из модуля FastAPI.responses.
# Внутри функции read_message мы определяем словарь, содержащий ключ
# сообщения со значением «Hello World». Затем мы возвращаем объект
# JSONResponse со словарем сообщений в качестве содержимого и кодом состояния
# 200.
