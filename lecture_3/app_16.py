# Использование форм WTForms в приложении
# В предыдущем пункте мы рассмотрели, как создавать формы с помощью WTForms.
# Теперь рассмотрим, как использовать эти формы в приложении Flask.
# Отображение форм на страницах приложения
# Для отображения формы на странице приложения необходимо создать объект
# формы в представлении и передать его в шаблон.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_3 import LoginForm

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


if __name__ == '__main__':
    app.run(debug=True)
# В данном примере определен маршрут /login, который обрабатывает GET и POST
# запросы. В представлении создается объект LoginForm, который передается в
# шаблон login.html с помощью функции render_template. Если метод запроса POST и
# данные формы проходят валидацию, то выполняется обработка данных из формы.
# Шаблон login.html должен содержать тег form с указанием метода и адреса для
# отправки данных формы, а также поля формы с помощью тегов input.
