# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def maximum():
    numbers = [x := int(input('Write a number: ')) for i in range(3)]
    print(numbers, max(numbers))

maximum()
# list_1 = [x.strip(',.*:;') for x in line.split() if x.replace('-', '').isdigit()]