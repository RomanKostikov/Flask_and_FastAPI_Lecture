# Выводим HTML
# Шаблонизатор Jinja
# Вывод сложных структур в цикле
# Иногда необходимо вывести информацию о нескольких однотипных объектах с
# набором свойств. Например, информацию о пользователях из базы данных. Или
# если упростить задачу, список словарей с одинаковыми ключами. Для опытных
# программистов очевидно, что оба вывода идентичны. Рассмотрим список словарей.
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "HI!"


@app.route('/users/')
def users():
    _users = [{'name': 'Никанор',
               'mail': 'nik@mail.ru',
               'phone': '+7-987-654-32-10',
               },

              {'name': 'Феофан',
               'mail': 'feo@mail.ru',
               'phone': '+7-987-444-33-22',
               },
              {'name': 'Оверран',
               'mail': 'forest@mail.ru',
               'phone': '+7-903-333-33-33',
               }, ]
    context = {'users': _users}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
# При выводе в шаблоне используем точечную нотацию для доступа к элементам
# списка словарей.
