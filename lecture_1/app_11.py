# Выводим HTML
# Шаблонизатор Jinja
# Для того, чтобы выводить эту пару страниц достаточно несколько строк кода на Flask

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "HI!"


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)


@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('data.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
# На каждой странице всего несколько различных строк в середине. Остальной код
# дублируется, Представьте, что у вас большой проект на десятки аналогичных
# страниц. Сколько же времени вы затратите, чтобы изменить шапку или футер во
# всём проекте?
