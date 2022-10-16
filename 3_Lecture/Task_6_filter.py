# filter - фильтрация последовательности
# filter(function, iterable)
# аргументы: функция фильтрации, последовательность

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

names = ['Leo', 'Max', 'Kate']
print(list(filter(lambda x: len(x) > 3, names)))