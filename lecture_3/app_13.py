# ➢Фильтрация данных
# Для фильтрации данных можно использовать метод filter() объекта запроса. Этот
# метод принимает условия фильтрации в виде аргументов или объектов-атрибутов
# модели.
from datetime import datetime, timedelta

from flask import Flask, render_template, jsonify
from lecture_3.models_05 import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content,
                         'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404


# Финальный пример фильтрации данных
@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title,
                         'content': post.content, 'created_at': post.created_at} for post
                        in posts])
    else:
        return jsonify({'error': 'Posts not found'})


if __name__ == '__main__':
    app.run(debug=True)

# Создаем маршрут /posts/last-week, который возвращает все посты, созданные за
# последнюю неделю. Внутри маршрута мы используем модуль datetime для
# вычисления даты, которая была неделю назад, и метод filter для фильтрации постов
# по дате создания. Если посты найдены, мы возвращаем их данные в формате JSON,
# иначе возвращаем ошибку.
# 🔥 Важно! Для работы без ошибок, добавьте строку импорта в начале файла:
# from datetime import datetime, timedelta
# Заключение по работе с Flask-SQLAlchemy
# Flask-SQLAlchemy — это мощный инструмент для работы с базами данных в
# приложениях Flask. Он предоставляет простой и удобный интерфейс для создания
# моделей, выполнения запросов и управления данными.
# Мы рассмотрели основные функции Flask-SQLAlchemy, такие как создание моделей,
# работу с данными, получение и фильтрацию данных. Мы также рассмотрели
# создание запросов к базе данных с помощью SQLAlchemy ORM.
# Flask-SQLAlchemy позволяет разработчикам быстро и легко создавать и
# поддерживать базы данных в своих приложениях Flask. Он также обеспечивает
# безопасность и надежность работы с данными.
