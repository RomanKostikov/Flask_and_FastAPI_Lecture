# Создание моделей
# При работе с Flask-SQLAlchemy необходимо определить модели данных, которые
# будут использоваться в приложении. Модель - это класс, который описывает
# структуру таблицы в базе данных.
# ➢Определение классов моделей
# Для определения модели необходимо создать класс, который наследует от класса
# Model из библиотеки SQLAlchemy. Название класса должно соответствовать
# названию таблицы в базе данных.
# Наполняем кодом models.py
# Пример:
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
    return f'User({self.username}, {self.email})'
# В этом примере определена модель User, которая имеет четыре поля: id, username,
# email и created_at. Поле id является первичным ключом таблицы и автоматически
# генерируется при добавлении записи в таблицу. Поля username и email являются
# строками с ограничением на уникальность и обязательность заполнения. Поле
# created_at содержит дату и время создания записи и автоматически заполняется
# текущей датой и временем при добавлении записи.
