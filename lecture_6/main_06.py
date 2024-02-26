# Работа с БД в CRUD операциях с SQLAlchemy
# и databases
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

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
# 💡 Внимание! По умолчанию SQLite разрешает взаимодействовать с ним
# только одному потоку, предполагая, что каждый поток будет обрабатывать
# независимый запрос. Это сделано для предотвращения случайного
# использования одного и того же соединения для разных вещей (для
# разных запросов). Но в FastAPI при использовании обычных функций (def)
# несколько потоков могут взаимодействовать с базой данных для одного и
# того же запроса, поэтому нам нужно сообщить SQLite, что он должен
# разрешать это с помощью connect_args={"check_same_thread": False}.
