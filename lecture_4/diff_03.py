# Загрузка в 5 процессов с использованием модуля multiprocessing:
import requests
from multiprocessing import Process, Pool
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://',
                                                '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
# Здесь мы используем модуль multiprocessing для создания процессов вместо
# потоков. Остальной код аналогичен предыдущему примеру.
# В результате выполнения кода мы получим следующее:
# Downloaded https://www.google.ru/ in 0.10 seconds
# Downloaded https://ya.ru/ in 0.20 seconds
# Downloaded https://www.python.org/ in 0.26 seconds
# Downloaded https://gb.ru/ in 0.53 seconds
# Downloaded https://habr.com/ru/all/ in 0.64 seconds
