# передать любое количество аргументов
# args - передача любого количества по порядку, формирует кортеж
# kwargs - передача любого количества по имени, формирует словарь

def greeting(say, *args):
    print(say, args)

greeting('Hello', 'Leo', 'Max', 'Kate')

def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

get_person(name='Leo', age=20)