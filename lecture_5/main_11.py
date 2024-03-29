# Определение конечных точек API
# Работа с параметрами запроса и путями URL
# Часто клиенты отправляют запросы с параметрами, которые нужно обработать на
# сервере. В FastAPI параметры запроса и пути URL определяются в декораторах
# конечных точек.
# Например:
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# Мы также можем определить несколько параметров URL-адреса в пути, например
# /users/{user_id}/orders/{order_id}, а затем определить соответствующие параметры в
# функции для доступа к ним.


@app.get("/users/{user_id}/orders/{order_id}")
async def read_item(user_id: int, order_id: int):
    # обработка данных
    return {"user_id": user_id, "order_id": order_id}
