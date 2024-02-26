# Устройство view функций
# Разберём подробнее как работаю функции представления.
# Маршрут (или путь) используется во фреймворке Flask для привязки URL-адреса к
# функции представления. Эта функция отвечает на запрос. Во Flask декоратор route()
# используется, чтобы связать URL с функцией.
# @app.route('/')
# def index():
#     return 'Привет, незнакомец!'
# Код назначает функцию index() обработчиком корневого URL в приложении. Когда
# приложение будет получать запрос, где путь — /, вызывается функция index(), и на
# этом запрос завершается.
# В следующем примере создано три маршрута в виде трёх отдельных view функций

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Ванечка!'


if __name__ == '__main__':
    app.run()
# Теперь при переходе по адресу http://127.0.0.1:5000/Иван/ в браузере будет
# открываться новая страница с приветствием.
# 🔥 Внимание! Если в строке браузера указать адрес без слеша на конце,
# сервер автоматически обработает адрес со слешем. Важно не забывать
# ставить слеш в конце адреса, который передаётся в route