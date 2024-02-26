# Несколько полезных функций
# Flash сообщения
# Flash сообщения в Flask являются способом передачи информации между
# запросами. Это может быть полезно, например, для вывода сообщений об
# успешном выполнении операции или об ошибках ввода данных.
# Для работы с flash сообщениями используется функция flash(). Она принимает
# сообщение и категорию, к которой это сообщение относится, и сохраняет его во
# временном хранилище.
# Например, чтобы вывести сообщение об успешной отправке формы, можно
# использовать следующий код:
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
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
# В этом примере мы определяем маршрут '/form' для отображения и обработки
# формы. Если метод запроса POST, то происходит обработка данных формы и
# выводится сообщение об успешной отправке с помощью функции flash() и
# категории 'success'. Затем происходит перенаправление на страницу с формой с
# помощью функции redirect().
# Секретный ключ
# Небольшое отступление. Чтобы не получать ошибки вида при работе с сессией
# RuntimeError: The session is unavailable because no secret key
# was set. Set the secret_key on the application to something
# unique and secret.
# необходимо добавить в Flask приложение секретный ключ.
# Простейший способ генерации такого ключа, выполнить следующие пару строк
# кода
