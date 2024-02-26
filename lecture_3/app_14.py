# Установка Flask-WTF
# Для установки Flask-WTF необходимо выполнить команду:
# pip install Flask-WTF
# После установки модуля его можно импортировать в приложение Flask:
from flask import Flask, render_template, jsonify
from flask_wtf import FlaskForm

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
