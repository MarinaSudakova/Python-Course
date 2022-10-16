# map - применение функции к каждому элементу последовательности
# map(func, iterable, ...)
# аргументы: функция, последовательность

numbers = [1, 5, 3, 5, 9, 7, 11]

print(list(map(lambda x: x ** 2, numbers)))

print(list(map(lambda x: str(x), numbers)))