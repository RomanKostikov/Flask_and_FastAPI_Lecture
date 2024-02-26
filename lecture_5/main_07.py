# Валидация данных запроса и ответа
# FastAPI позволяет автоматически валидировать данные запроса и ответа с
# помощью модуля pydantic. Например, можно создать класс Item для валидации
# данных:
# ...
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# ...
