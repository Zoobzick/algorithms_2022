"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для четвертого скрипта
"""
from pympler import asizeof


# из курса Основ Python. Урок 5, 5 задание.
# Исходное решение
def my_filter(*arg):
    filtered = set()
    for el in arg:
        if el not in filtered:
            filtered.add(el)
        else:
            filtered.discard(el)
    return (i for i in filtered if i in filtered)

# Оптимизированное решение
def my_filter_2(*arg):
    return list(filter(lambda x: src.count(x) > 1, src))


src = [2, 2, 2, 7, 23, 1, 1, 1, 1, 1, 44, 44, 3, 2, 10, 7, 4, 11, 11, 11, 11, 11]

print(asizeof.asizeof(my_filter()))
print(asizeof.asizeof(my_filter_2()))

"""
Применение filter уменьшает расход памяти в два раза
"""