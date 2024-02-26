# Установка и настройка
# ➢Установка Flask-SQLAlchemy
# Для установки Flask-SQLAlchemy необходимо выполнить команду:
# pip install Flask-SQLAlchemy # Widows
# pip3 install Flask-SQLAlchemy # Unix
# После этого можно импортировать его в свой проект:
# from flask_sqlalchemy import SQLAlchemy
# ➢Настройка подключения к базе данных
# Для настройки подключения к базе данных необходимо указать адрес базы данных,
# а также ее тип и некоторые другие параметры. Например, для подключения к базе
# данных SQLite можно использовать следующий код:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://username:password@hostname/database_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@hostname/database_name'
db = SQLAlchemy(app)
...


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
# В данном примере мы создаем объект app класса Flask, указываем адрес базы
# данных в параметре SQLALCHEMY_DATABASE_URI и создаем объект db класса
# SQLAlchemy.
# Адрес базы данных может быть различным в зависимости от ее типа и места
# расположения. В данном примере мы используем базу данных SQLite, которая
# хранится в файле mydatabase.db в текущей директории.
# Также можно использовать другие типы баз данных, такие как MySQL, PostgreSQL и
# другие. Для этого необходимо указать соответствующий адрес и параметры
# подключения.
# Например, для подключения к базе данных MySQL можно использовать следующий
# код:
# ...
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =
# 'mysql+pymysql://username:password@hostname/database_name'
# db = SQLAlchemy(app)
# ...
# Здесь мы указываем адрес базы данных в формате:
# mysql+pymysql://username:password@hostname/database_name, где
# username и password - это логин и пароль для подключения к базе данных,
# hostname - адрес сервера базы данных, а database_name - имя базы данных.
# При подключении к PostgreSQL используется аналогичная строка. Изменяется лишь
# начало:
# postgresql+psycopg2://username:password@hostname/database_name
