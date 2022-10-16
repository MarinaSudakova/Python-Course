# abs - модуль числа
# min, max - минимальное и максимаьное значение
# round - округление
# sum - сумма элементов поледовательности
# enumerate - нумерация последовательносьти

# Пользователь вводит 3 числа. Найти минимальное из них, максимальное из них, их сумму и вывести результат на экран
numbers = []
for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(max(numbers))
print(min(numbers))
print(sum(numbers))