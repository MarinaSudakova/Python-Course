# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. 
# Поэкспериментируйте с значениями урона и жизней по желанию. 
# Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. 
# Функция в качестве аргумента будет принимать атакующего и атакуемого. 
# В теле функция должна получить параметр damage атакующего и отнять это количество от 
# health атакуемого. Функция должна сама работать со словарями и изменять их значения.

player_mame = input('Write player name: ')

player = {
    'name' : player_mame,
    'health' : 100,
    'damage': 50,
    'armor': 1.2
}

enemy_mame = input('Write enemy name: ')
enemy = {
    'name' : enemy_mame,
    'health' : 100,
    'damage': 50,
    'armor': 1.3
}

def attack(unit, target):
    x = unit['damage'] / target['armor']
    target['health'] -= x

attack(player, enemy)
print(enemy)