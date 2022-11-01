#Игра угадай число

import random

number = random.randint(1, 100)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input("Write a level of game: "))
max_count = levels[level]

user_count = int(input('Write count of gamers: '))
users = []
for i in range(1, user_count + 1):
    user_name = input(f'Write name of {i} gamer: ')
    users.append(user_name)

print(users)
is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print("All gamers loose")
        break
    print(f'Trying # {count}')
    for user in users:
        print(f'Move of {user}')
        user_number = int(input('Write a number: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Your number is bigger')
        elif number > user_number:
            print('Your number is lower')

else: #конструкция сработает только если цикл закончился по главному условию
    print(f'{winner_name} you are right!')