# sorted - сортировка последовательности
# sorted(iterable, *, key=None, reverse=False)
# аргументы: последовательность, ключ для сортировки, порядок

numbers = [1, 5, 3, 5, 9, 7, 11]
# по возрастанию
print(sorted(numbers))
# по убыванию
print(sorted(numbers, reverse=True))

# c доп параметром
cities = [('Moscow', 1000), ('Las-Vegas', 5000), ('Tokio', 7000)]
print(sorted(cities))

def by_count(city):
    return city[1]

print(sorted(cities, key=by_count))

print(sorted(cities, key=lambda x: x[1]))
