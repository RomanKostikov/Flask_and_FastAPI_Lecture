# Работа с БД в CRUD операциях с SQLAlchemy
# и databases

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)


# Добавление тестовых пользователей в БД
# Прежде чем работать над созданием API и проходить всю цепочку CRUD для
# клиента сгенерируем несколько тестовых пользователей в базе данных.
@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}',
                                      email=f'mail{i}@mail.ru')
        await database.execute(query)
    return {'message': f'{count} fake users create'}
# Принимаем целое число count и создаём в БД указанное число пользователей с
# именами и почтами. Теперь мы готовы не только разрабатывать CRUD, но и
# тестировать его.
# 🔥 Важно! Не забудьте перейти по адресу http://127.0.0.1:8000/fake_users/25
# чтобы добавить пользователей.
# 💡 Внимание! В реальном проекте подобные функции должны быть
# отключены перед запускам в продакшен.
