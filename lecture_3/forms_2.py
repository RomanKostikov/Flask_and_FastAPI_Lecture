# Создание форм в WTForms
# Описание полей форм
# WTForms предоставляет множество типов полей для формы. Вот некоторые из них:
# ● StringField — строковое поле для ввода текста;
# ● IntegerField — числовое поле для ввода целочисленных значений;
# ● FloatField — числовое поле для ввода дробных значений;
# ● BooleanField — чекбокс;
# ● SelectField — выпадающий список;
# ● DateField — поле для ввода даты;
# ● FileField — поле для загрузки файла.
# Рассмотрим ещё один пример создания форм:
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])
# В данном примере определен класс RegisterForm, который наследуется от
# FlaskForm. Внутри класса определены три поля: name, age и gender. Поле name
# является строковым полем, поле age — числовым, а поле gender — выпадающим
# списком. В списке выбора есть две опции: male и female.
