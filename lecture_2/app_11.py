# Несколько полезных функций
# Перенаправления
# Перенаправления в Framework Flask позволяют перенаправлять пользователя с
# одной страницы на другую. Это может быть полезно, например, для
# перенаправления пользователя после успешной отправки формы или для
# перенаправления пользователя на страницу авторизации при попытке доступа к
# защищенной странице без авторизации.
# Для перенаправления в Flask используется функция redirect(). Она принимает
# URL-адрес, на который нужно перенаправить пользователя, и возвращает объект
# ответа, который перенаправляет пользователя на указанный адрес.
# Например, чтобы перенаправить пользователя на главную страницу сайта, можно
# использовать следующий код:
from flask import Flask, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external/')
def external_redirect():
    return redirect('https://www.python.org')


@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'


@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
# В этом примере мы определяем два маршрута: '/' для главной страницы и '/redirect'
# для перенаправления на главную страницу. Функция redirect_to_index() использует
# функцию redirect() для перенаправления пользователя на главную страницу с
# помощью функции url_for(), которая возвращает URL-адрес для указанного
# маршрута.
# Функция redirect() также может использоваться для перенаправления пользователя
# на внешний URL-адрес. Например:
# ...
# @app.route('/external')
# def external_redirect():
# return redirect('https://google.com')
# ```
# В этом примере мы используем функцию redirect() для перенаправления
# пользователя на внешний URL-адрес https://google.com.
