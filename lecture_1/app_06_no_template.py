# Выводим HTML
# Начнём с того, что импортируем функцию отрисовки шаблонов. render_template()
# принимает в качестве первого аргумента название html-файла, который
# необходимо вывести в браузер.
# from flask import render_template
# Добавим функцию рендеринга в функцию представления и укажем ей на файл
# index.html. Общий код будет выглядеть так:
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/index/')
def html_index():
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)
# После перехода по локальному адресу получим сообщение об ошибке:
# TemplateNotFound
# jinja2.exceptions.TemplateNotFound: index.html
# Функция render_template() ищет файл index.html в папке templates. Необходимо
# перенести его в нужную папку. Другие html-файлы также необходимо складывать в
# указанную папку.
# После перезагрузки сервер выводит страницу в браузер.
# 🔥 Внимание! Если изображения или стили отсутствуют, необходимо
# переместить их в соответствующие каталоги: стили в static/css, а
# изображения — в static/image. В самом html проверить путь к файлам:
# <link rel="stylesheet" href="/static/css/style.css">
# <img src="/static/image/foto.png" alt="Моё фото" width="300">
# После очередной перезагрузки сервера мы получим полноценную html-страницу.
