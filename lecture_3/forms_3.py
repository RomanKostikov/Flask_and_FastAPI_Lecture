# Создание форм в WTForms
# Валидация данных формы
# WTForms позволяет проводить валидацию данных формы. Для этого можно
# использовать готовые валидаторы, такие как DataRequired, Email, Length и другие.
# Также можно написать свой собственный валидатор.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

# pip install email-validator
# В данном примере определен класс RegistrationForm, который наследуется от
# FlaskForm. Внутри класса определены три поля: email, password и confirm_password.
# Поле email проверяется на наличие данных и на соответствие формату email. Поле
# password проверяется на наличие данных и на минимальную длину (6 символов).
# Поле confirm_password проверяется на наличие данных и на соответствие значению
# поля password.
# 🔥 Важно! Для правильной работы кода необходимо отдельно установить
# валидатор электронной почты. Для этого достаточно выполнить команду:
# pip install email-validator
# 💡 Внимание! В валидатор EqualTo передаётся строковое имя переменной,
# т.е. то, что стоит слева от знака равно, а не название поля
# WTForms — мощная библиотека для создания HTML-форм и их валидации в Flask.
# Определение классов форм является основой работы с библиотекой. Описание
# полей форм и проведение их валидации позволяют создавать надежные и удобные
# для пользователей формы
