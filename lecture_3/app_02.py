# Внутри основного файла проекта оставим следующий код:
from flask import Flask
from lecture_3.models_02 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
# 🔥 Важно! Теперь класс не получает приложение Flask app при
# инициализации. Для инициализации баз данных необходимо выполнить
# строку db.init_app(app)
