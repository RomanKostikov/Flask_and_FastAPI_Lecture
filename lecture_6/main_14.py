# Больше про валидацию данных
# Пример 1:
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., ge=1), q: str = None):
    return {"item_id": item_id, "q": q}
# В этом примере мы создаем маршрут "/items/{item_id}" с параметром пути "item_id".
# Параметр "item_id" имеет тип int и должен быть больше или равен 1. Мы используем
# многоточие (...) в качестве значения по умолчанию для параметра "item_id", что
# означает, что параметр обязателен для передачи в URL. Если параметр не передан
# или его значение меньше 1, то будет сгенерировано исключение.