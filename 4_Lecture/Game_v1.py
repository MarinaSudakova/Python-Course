#Игра угадай число

import random

number = random.randint(1, 100)



while True:
    user_number = int(input('Write a number: '))
    if number == user_number:
        print('You are right')
        break
    elif number < user_number:
        print('Your number is bigger')
    else:
        print('Your number is lower')