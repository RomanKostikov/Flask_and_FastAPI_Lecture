# Обычная синхронная загрузка:
import requests
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]
start_time = time.time()
for url in urls:
    response = requests.get(url)
    filename = 'sync_' + url.replace('https://', '').replace('.',
                                                             '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
# В данном примере мы используем библиотеку requests для получения
# html-страницы каждого сайта из списка urls. Затем мы записываем полученный
# текст в файл с именем, соответствующим названию сайта.
# 🔥 Важно! Используйте pip install requests, если не устанавливали библиотеку
# ранее.
# Здесь мы получаем следующее:
# Downloaded https://www.google.ru/ in 0.08 seconds
# Downloaded https://gb.ru/ in 0.55 seconds
# Downloaded https://ya.ru/ in 0.72 seconds
# Downloaded https://www.python.org/ in 0.94 seconds
# Downloaded https://habr.com/ru/all/ in 1.68 seconds