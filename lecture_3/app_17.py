# Использование форм WTForms в приложении
# Обработка данных из формы
# Для обработки данных из формы необходимо получить данные из объекта request и
# провести их валидацию с помощью метода validate() объекта формы.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_3 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c7f0a9fe796da138a935cdf5e0d73a03b202ec4bb60ad9c7626ac18b2881f2eb'
csrf = CSRFProtect(app)

"""
Генерация токена
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
# В отличии от шаблона login.html мы не указываем поля явно. После стандартного
# вывода csrf токена создаём цикл для по всем полям формы за исключением токена.
# Для каждого поля выводится метка и окно поле ввода. Отдельно проверяем
# наличие ошибок ввода и если они есть, в цикле выводим все ошибки для каждого
# из полей. Таким образом мы динамически формируем страницу регистрации. А в
# случае неверного ввода данных пользователем, сразу сообщаем ему об ошибках.
# WTForms позволяет легко создавать и валидировать HTML-формы в приложении
# Flask. Для отображения форм на страницах приложения необходимо создать объект
# формы в представлении и передать его в шаблон. Для обработки данных из формы
# необходимо получить данные через post запрос и провести их валидацию с
# помощью метода validate() объекта формы.
