# Создание форм в WTForms
# WTForms — это библиотека Python, которая позволяет создавать HTML-формы, а
# также проводить их валидацию. Flask-WTF использует WTForms для создания форм.
# Определение классов форм
# Для создания формы с помощью Flask-WTF необходимо определить класс формы,
# который наследуется от класса FlaskForm. Каждое поле формы определяется как
# экземпляр класса, который наследуется от класса Field.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
# В данном примере определен класс LoginForm, который наследуется от FlaskForm.
# Внутри класса определены два поля: username и password. Поле username является
# строковым полем, а поле password — полем для ввода пароля. Оба поля
# обязательны для заполнения, так как им передан валидатор DataRequired.
