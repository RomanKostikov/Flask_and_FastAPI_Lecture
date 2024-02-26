# ➢Фильтрация данных
# Для фильтрации данных можно использовать метод filter() объекта запроса. Этот
# метод принимает условия фильтрации в виде аргументов или объектов-атрибутов
# модели.
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


if __name__ == '__main__':
    app.run(debug=True)
# В этом примере получаем все объекты модели User из базы данных, у которых имя
# пользователя равно username из строки запроса, с помощью метода filter() и
# выводим их имена пользователей и электронные адреса используя прежний
# шаблон.
# Мы создаем маршрут /posts/author/<int:user_id>, который принимает ID
# пользователя в качестве параметра. Внутри маршрута мы используем метод
# filter_by для фильтрации постов по ID автора и метод all для получения всех
# найденных постов. Если посты найдены, мы возвращаем их данные в формате
# JSON, иначе возвращаем ошибку.
# 🔥 Внимание! Для того, чтобы вернуть JSON объект используется функция
# jsonify. Её необходимо импортировать из модуля Flask перед
# использованием
