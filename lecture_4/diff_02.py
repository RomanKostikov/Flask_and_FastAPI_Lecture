# Загрузка в 5 потоков с использованием модуля threading:
import requests
import threading
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://',
                                          '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
# Здесь мы создаем функцию download, которая загружает html-страницу и сохраняет
# ее в файл. Затем мы создаем по одному потоку для каждого сайта из списка urls,
# передавая функцию download в качестве целевой функции для каждого потока. Мы
# запускаем каждый поток и добавляем его в список threads. В конце мы ждем
# завершения всех потоков с помощью метода join.
# В результате выполнения кода мы получим следующее:
# Downloaded https://www.google.ru/ in 0.10 seconds
# Downloaded https://www.python.org/ in 0.23 seconds
# Downloaded https://ya.ru/ in 0.30 seconds
# Downloaded https://habr.com/ru/all/ in 0.47 seconds
# Downloaded https://gb.ru/ in 0.81 seconds