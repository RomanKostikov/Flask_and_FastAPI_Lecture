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


# Создание моделей для взаимодействия с таблицей в БД
# Создадим две модели данных Pydantic:
class UserIn(BaseModel):
    name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)
# Первая модель нужна для получения информации о пользователе от клиента. А
# вторая используется для возврата данных о пользователе из БД клиенту.
