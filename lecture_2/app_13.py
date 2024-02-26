# Несколько полезных функций
# Flash сообщения
# Категории flash сообщений
# Категории сообщений в flash позволяют различать типы сообщений и выводить их
# по-разному. Категория по умолчанию message. Но вторым аргументом можно
# передавать и другие категории, например warning, success и другие.
# Например, чтобы вывести сообщение об ошибке ввода данных, можно
# использовать следующую модификацию функции:
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = b'16598d160e54de72120c829a1baa9ffa810ecf73b3dc43121022f011277914bc'
"""
Генерация секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
# Проверяем данные формы на наличие имени. Если имя не указано, то выводится
# сообщение об ошибке с категорией danger и происходит перенаправление на
# страницу с формой. Сама форма будет работать без изменений.
# Flash сообщения являются удобным способом передачи информации между
# запросами в Flask. Они позволяют выводить сообщения пользователю и упрощают
# обработку ошибок и успешных операций.
