# Пример 3:
import random
import time


def long_running_task():
    for i in range(5):
        print(f"Выполнение задачи {i}")
        time.sleep(random.randint(1, 3))


def main():
    print("Начало программы")
    long_running_task()
    print("Конец программы")


main()
# Эта программа запускает длительную задачу long_running_task(), которая
# выполняется в течение случайного времени от 1 до 3 секунд. Весь код работает
# синхронно, поэтому выполнение программы блокируется на время выполнения
# задачи.
# В целом, синхронный код может быть полезен для простых задач, но он может стать
# проблемой при работе с длительными операциями или задачами, требующими
# большого количества вычислений. В таких случаях лучше использовать
# многопоточный или асинхронный код.