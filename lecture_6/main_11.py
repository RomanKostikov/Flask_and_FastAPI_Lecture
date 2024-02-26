# Работа с БД в CRUD операциях с SQLAlchemy
# и databases
from typing import List

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
# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user{i}',
#                                       email=f'mail{i}@mail.ru')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}
# ➢Создание пользователя в БД, create
# Чтобы создать нового пользователя в таблице «users», мы можем определить
# функцию следующим образом:
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name,
                                  email=user.email)
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


# ➢Чтение одного пользователя из БД, read
# Чтобы прочитать одного пользователей из таблицы «users», мы можем определить
# функцию следующим образом:

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)
# Мы определяем маршрут "/users/{user_id}" для чтения одного пользователя по его
# ID. В параметре функции мы ожидаем передачу ID пользователя. Затем мы создаем
# SQL-запрос на выборку записи из таблицы "users" с указанным ID. Выполняем
# запрос и возвращаем полученные данные в виде объекта типа User.
