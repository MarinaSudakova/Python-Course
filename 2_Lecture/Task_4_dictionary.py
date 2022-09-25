friends = ['Max', 'Leo', 'Kate']
friend = friends[0]

friend = {
    'name': 'Max',
    'age': 23
}

print(friend)
print(type(friend))

# получить элемент словаря по ключу
print(friend['age'])

# добавить или изменить элемент по ключу
friend['has_car'] = True
print(friend)

# удалить элемент словаря
del friend['age']
print(friend)

# цикл for по ключам, будет работать и без доп функции
for key in friend.keys():
    print(key)

# цикл for по значениям, будет работать и без доп функции
for val in friend.values():
    print(val)

# цикл for по значениям и по ключам
for key, val in friend.items():
    print(key, val)
