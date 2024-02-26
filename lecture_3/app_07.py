# ➢Изменение записей
# Для изменения существующей записи нужно получить ее из базы данных, изменить
# нужные поля и вызвать метод commit().


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


@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')


if __name__ == '__main__':
    app.run(debug=True)
# В этом примере получаем объект модели User по имени пользователя "john",
# изменяем его электронную почту на "new_email@example.com" и сохраняем
# изменения с помощью метода commit().
# 🔥 Внимание! Если бы база данных позволяла хранить несколько
# пользователей с одинаковыми username, в переменную user попал бы один
# пользователь благодаря методу first().
