# len(friends) - длина списка (сколько в нем элементов)
# friends.append(‘Ron’) - добавление нового элемента
# friends.pop() - удаляем последний элемент и возвращаем его
# friends.clear() - очищаем весь список
# friends.remove(‘Ron’) - удаление объекта из списка
# del friends[0] - удаление элемента по индексу

# использование оператора in

hero = 'Superman'

if 'man' in hero:
    print('Yes')

# кортеж защищает список от изменений и пишется в круглых скобках

print('Соревнования по пайтон')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место '.format(i))
    members.append(name)
    i-=1

print('В сорвеновании участвовали: ', sorted(members))
members.reverse() # разворачиваем список
result = members[:3]
result = 'Победители : {}. Поздравляем!'.format(result)
print(result)