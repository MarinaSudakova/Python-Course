#Игра угадай число

import random

number = random.randint(1, 100)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input("Write a level of game: "))
max_count = levels[level]

while number != user_number:
    count += 1
    print(f'Trying # {count}')
    if count > max_count:
        print("You loose")
        break
    user_number = int(input('Write a number: '))
    if number < user_number:
        print('Your number is bigger')
    elif number > user_number:
        print('Your number is lower')

else: #конструкция сработает только если цикл закончился по главному условию
    print('You are right!')