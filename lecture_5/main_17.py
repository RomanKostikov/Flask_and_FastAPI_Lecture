# Автоматическая документация по API
# Пример использования
# Для генерации документации нужно создать экземпляр класса FastAPI с
# параметром openapi_url:
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.get("/hello/{name}")
async def read_item(name: str, age: int):
    return {"Hello": name, "Age": age}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
# В этом примере мы переопределили метод custom_openapi, который генерирует
# схему OpenAPI вручную. Мы также установили значение параметра openapi_url,
# чтобы FastAPI знал, где разместить схему OpenAPI.
# После запуска приложения можно перейти по адресу
# http://localhost:8000/api/v1/openapi.json и убедиться, что схема OpenAPI была
# успешно сгенерирована.
# Затем можно запустить приложение и перейти по адресу http://localhost:8000/docs
# или http://localhost:8000/redoc, чтобы просмотреть сгенерированную
# документацию.
