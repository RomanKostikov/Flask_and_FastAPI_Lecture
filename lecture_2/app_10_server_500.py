# Несколько полезных функций
# В этой главе рассмотрим несколько полезных функций, которые сделают ваше
# приложение лучше.
# Обработка ошибок
# Некоторые коды ошибок
# ● 400: Неверный запрос
# ● 401: Не авторизован
# ● 403: Доступ запрещен
# ● 404: Страница не найдена
# ● 500: Внутренняя ошибка сервера
# Иногда из-за ошибок в коде сервер может возвращать ошибку 500. В идеальном
# мире код предусматривает все возможные ситуации и не отдаёт ошибку 500. Но
# почему бы не подстелить соломки.
# Удалим функции get_blog из примера выше. Теперь при попытке найти статью по id
# получаем сообщение на странице:
# Internal Server Error
# The server encountered an internal error and was unable to complete your request.
# Either the server is overloaded or there is an error in the application.
# 🔥 Важно! Если вы запускаете сервер в режиме отладки, будет выведена
# трассировка ошибки, а не сообщение. Перезапустите сервер с параметром
# debug=False
# В несколько строк напишем обработчик для вывода сообщения в стиле проекта.
import logging
from flask import Flask, render_template, request, abort

# from lecture_2.db import get_blog

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    ...
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)
    ...


# возвращаем найденную в БД статью
@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)
# По сути взяли за основу обработчик ошибки 404, но лог фиксирует не
# предупреждение, а ошибку. Плюс новый шаблон, и возврат кода 500 клиенту
