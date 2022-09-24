# Запросите от пользователя число, сохраните в переменную, 
# прибавьте к числу 2 и выведите результат на экран.

number = int(input("Введите число: "))
print('Введеный', number, 'при сложении с двойкой станет', number+2)

# Используя цикл, запрашивайте у пользователя число, 
#пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, 
# возведите его в степень 2 и выведите на экран.

num = int(input("Введите число от 1 до 9: "))
while num <= 0 or num >= 10:
    num = int(input('Ошибка, попробуйте снова: '))
else:
    print(num**2)

# “Медицинская анкета”
name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))

if age < 30 and weight > 50 and weight < 120:
    print(name, surname, sep=',', end=',')
    print(age, 'год', end=',',)
    print('год', weight, end=',',)
    print(" - хоршее состояние")
elif age > 30 and (weight < 50 or weight > 120):
    print(name, surname, sep=',', end=',')
    print(age, 'год', end=',',)
    print('вес', weight, end=',',)
    print(" - займитесь собой")
elif age > 40 and (weight < 50 or weight > 120):
    print(name, surname, sep=',', end=',')
    print(age, 'год', end=',',)
    print('вес', weight, end=',',)
    print(" - нужен доктор")    
else:
    print('что с вами делать?')
