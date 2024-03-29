# Урок 4. Введение в многозадачность

## Classwork

### Теория:

#### Введение в многозадачность в Python

В современном программировании часто возникает необходимость выполнять
несколько задач одновременно. Для этого используется многозадачность —
способность компьютера или программы обрабатывать несколько задач
одновременно.
В Python существует несколько подходов к реализации многозадачности, каждый
из которых имеет свои преимущества и недостатки. Прежде чем начать
использовать многозадачность в своих программах, необходимо понимать
основные понятия и подходы.

* Поток выполнения — это независимая последовательность инструкций, которая
  может выполняться параллельно с другими потоками. Каждый поток имеет свой
  стек вызовов и свой контекст выполнения.
* Процесс — это экземпляр программы, который запущен на компьютере. Каждый
  процесс имеет свой собственный адресное пространство, в котором хранятся
  данные и код программы. Процессы могут выполняться параллельно на разных
  ядрах процессора.
  Далее рассмотрим различные подходы к многозадачности в Python и их
  применение в различных ситуациях.

#### Синхронный подход

Синхронный код — это код, который выполняется последовательно, одна операция
за другой. Когда программа выполняет какую-то операцию, она блокируется до тех
пор, пока операция не будет завершена. Таким образом, если в программе есть
долгие операции, они могут занимать много времени и приводить к задержкам в
работе программы.
Примеры синхронных операций в Python:
● чтение данных из файла
● отправка запроса на сервер и получение ответа
● выполнение сложных математических операций
● ожидание пользовательского ввода
Ограничения синхронного кода:
● задержки в работе программы из-за долгих операций
● невозможность выполнения нескольких задач одновременно
● ограниченность производительности
Для решения этих проблем можно использовать многопоточный или
многопроцессорный подход. Однако, при использовании многопоточности и
многопроцессорности возникают свои проблемы, такие как конкуренция за
ресурсы и возможные блокировки.

#### Многопоточный подход

Многопоточный код — это подход к многозадачности, при котором программа
может выполнять несколько задач одновременно в разных потоках выполнения.
Каждый поток выполняет свою задачу независимо от других потоков, что позволяет
улучшить производительность программы.
Примеры многопоточных операций в Python:
● загрузка данных из нескольких файлов одновременно
● параллельная обработка большого объема данных
● одновременное выполнение нескольких запросов к базе данных
● многопоточный веб-сервер, обрабатывающий несколько запросов
одновременно
Преимущества многопоточного кода:
● увеличение производительности программы за счет параллельного
выполнения задач
● возможность выполнения нескольких задач одновременно без блокировки
Недостатки многопоточного кода:
● возможность возникновения конкуренции за ресурсы
● сложность отладки и тестирования многопоточных программ
● возможность блокировки потоков выполнения
Для решения проблем, связанных с конкуренцией за ресурсы и блокировками
потоков, можно использовать механизмы синхронизации, такие как блокировки и
семафоры. Однако, неправильное использование этих механизмов может привести
к дедлокам (deadlock) и другим проблемам.
При разработке многопоточных программ необходимо учитывать особенности
языка Python, такие как GIL (Global Interpreter Lock), который ограничивает
параллелизм в исполнении Python-кода. Это означает, что в Python нельзя
использовать несколько ядер процессора для выполнения одной программы.
В целом, многопоточный подход позволяет улучшить производительность
программы и выполнить несколько задач одновременно без блокировки. Однако,
при разработке многопоточных программ необходимо учитывать особенности
языка Python и правильно использовать механизмы синхронизации для избежания
проблем.

#### Многопроцессорный подход

Многопроцессорный код — это подход к многозадачности, при котором программа
может выполнять несколько задач одновременно в разных процессах. Каждый
процесс выполняет свою задачу независимо от других процессов, что позволяет
улучшить производительность программы. При этом процессы могут быть
запущены на разных процессорах многопроцессорного сервера.
Примеры многопроцессорных операций в Python:
● параллельная обработка большого объема данных
● одновременное выполнение нескольких запросов к базе данных
● многопроцессорный веб-сервер, обрабатывающий несколько запросов
одновременно
Преимущества многопроцессорного кода:
● возможность использования нескольких ядер процессора для выполнения
программы
● увеличение производительности программы за счет параллельного
выполнения задач
● возможность выполнения нескольких задач одновременно без блокировки
Недостатки многопроцессорного кода:
● возможность возникновения конкуренции за ресурсы
● сложность управления и координации процессов
● возможность блокировки процессов выполнения
Для решения проблем, связанных с конкуренцией за ресурсы и блокировками
процессов, можно использовать механизмы синхронизации, такие как блокировки
и семафоры. Однако, неправильное использование этих механизмов может
привести к дедлокам (deadlock) и другим проблемам.
При разработке многопроцессорных программ необходимо учитывать особенности
языка Python, такие как использование модуля multiprocessing для создания и
управления процессами. Также следует учитывать потребление ресурсов
процессами и оптимизировать их работу.
В целом, многопроцессорный подход позволяет использовать несколько ядер
процессора для выполнения программы и улучшить ее производительность.
Однако, при разработке многопроцессорных программ необходимо учитывать
особенности языка Python и правильно использовать механизмы синхронизации
для избежания проблем.

#### Асинхронный подход

Асинхронный код — это подход к многозадачности, при котором программа может
выполнять несколько задач одновременно без создания отдельных процессов или
потоков. Вместо этого задачи выполняются в рамках одного потока выполнения, но
с использованием механизмов событий и обратных вызовов.
Примеры асинхронных операций в Python:
● обработка сетевых запросов
● чтение и запись в файлы
● обработка пользовательских событий в графическом интерфейсе
Преимущества асинхронного кода:
● более эффективное использование ресурсов процессора и памяти
● возможность обрабатывать большое количество задач одновременно без
создания отдельных процессов или потоков
● упрощение кода и улучшение его читаемости
Недостатки асинхронного кода:
● сложность отладки и тестирования
● возможность возникновения ошибок из-за неправильного использования
механизмов событий и обратных вызовов
● ограниченная поддержка сторонними библиотеками
Для разработки асинхронного кода в Python используется модуль asyncio, который
предоставляет механизмы для организации асинхронного выполнения задач.
Ключевыми понятиями в asyncio являются корутины, события и цикл событий.
Корутины — это функции, которые могут приостанавливать свое выполнение,
чтобы дать возможность другим корутинам выполниться.
События используются для уведомления корутин о том, что какое-то событие
произошло (например, завершение сетевого запроса).
Цикл событий — это основной механизм, который управляет выполнением корутин
и обработкой событий.
При разработке асинхронного кода необходимо учитывать особенности работы с
корутинами и правильно использовать механизмы событий для избежания
проблем. Также следует учитывать поддержку сторонними библиотеками и
оптимизировать работу программы.
В целом, асинхронный подход позволяет эффективно использовать ресурсы
процессора и памяти, обрабатывать большое количество задач одновременно и
упрощать код. Однако, при разработке асинхронного кода необходимо учитывать
особенности работы с корутинами и правильно использовать механизмы событий
для избежания проблем.

#### Сравнение разных подходов на примере парсинга сайтов

Перед нами задача по скачиванию информации с главных страниц пяти сайтов.
Рассмотрим решение задачи с использованием синхронного, многопоточного,
многопроцессорного и асинхронного подходов.
