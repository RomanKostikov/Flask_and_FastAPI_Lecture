# ➢Создание таблиц в базе данных
# Остался финальный этап. Напишим функцию, которая создаст таблицы через
# консольную команду. Заполняем основной файл проекта
from flask import Flask
from lecture_3.models_05 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'


@app.cli.command("init-db")
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)
# 🔥 Важно! Теперь класс не получает приложение Flask app при
# инициализации. Для инициализации баз данных необходимо выполнить
# строку db.init_app(app)
