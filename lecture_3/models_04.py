# Создание моделей
# ➢Описание полей моделей
# Для описания полей модели используются классы-типы данных из библиотеки
# SQLAlchemy. Существуют следующие типы данных:
# ● Integer — целое число
# ● String — строка
# ● Text — текстовое поле
# ● Boolean — булево значение
# ● DateTime — дата и время
# ● Float — число с плавающей точкой
# ● Decimal — десятичное число
# ● Enum — перечисление значений
# ● ForeignKey — внешний ключ к другой таблице
# Рассмотрим ещё один пример таблицы:
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='user', lazy=True)  # новая строка


def __repr__(self):
    return f'User({self.username}, {self.email})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
    return f'Post({self.title}, {self.content})'

# В этом примере определена модель Post, которая имеет пять полей: id, title, content,
# author_id и created_at. Поля title и content являются строками и обязательны для
# заполнения. Поле author_id является внешним ключом к таблице пользователей
# (User) и ссылается на поле id этой таблицы. Поле created_at содержит дату и время
# создания записи и автоматически заполняется текущей датой и временем при
# добавлении записи.
# К моделе пользователя добавим следующую строку:
# posts = db.relationship('Post', backref='author', lazy=True)
# Так мы (а точнее наш код) понимаем какие посты принадлежат конкретному
# пользователю.
