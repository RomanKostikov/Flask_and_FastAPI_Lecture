# ➢Создание записей
# Для создания новой записи в базе данных необходимо создать объект модели и
# добавить его в сессию базы данных. После этого нужно вызвать метод commit() для
# сохранения изменений.

from flask import Flask
from lecture_3.models_05 import db, User

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


@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


if __name__ == '__main__':
    app.run(debug=True)
# В этом примере создается новый объект модели User с именем пользователя "john"
# и электронной почтой "john@example.com". Затем объект добавляется в сессию
# базы данных и сохраняется с помощью метода commit().
# Как вы уже догадались для выполнения функции необходимо выполнить в консоли
# команду flask add-john
