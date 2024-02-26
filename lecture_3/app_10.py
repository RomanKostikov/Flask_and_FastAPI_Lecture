# ➢Получение данных из базы данных
# Для получения данных из базы данных необходимо использовать метод query()
# модели. Этот метод возвращает объект запроса, который можно дополнить
# фильтрами и другими параметрами.
from flask import Flask, render_template
from lecture_3.models_05 import db, User

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


if __name__ == '__main__':
    app.run(debug=True)
