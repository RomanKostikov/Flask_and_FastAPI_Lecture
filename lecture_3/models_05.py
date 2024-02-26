# Создание моделей
# ➢Создание связей между моделями
# Для создания связей между моделями используется поле ForeignKey. Оно указывает
# на поле первичного ключа связанной таблицы.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)  # новая строка


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


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
    return f'Comment({self.content})'

# В этом примере определена модель Comment, которая имеет пять полей: id, content,
# post_id, author_id и created_at. Поля content и post_id являются обязательными для
# заполнения. Поле post_id является внешним ключом к таблице постов (Post) и
# ссылается на поле id этой таблицы. Поле author_id является внешним ключом к
# таблице пользователей (User) и ссылается на поле id этой таблицы. Поле created_at
# содержит дату и время создания записи и автоматически заполняется текущей
# датой и временем при добавлении записи.
