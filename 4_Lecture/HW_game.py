# В этой игре человек загадывает число, а компьютер пытается его угадать.

print("Create a integer from 1 to 100, but don't tell it")
trying = int(input('How many trying can you give me? '))
print('Ok')

user_number = False
number = 0
count = 0
min = 0
max = 100
token = 0


while not user_number:
    count += 1
    if count > trying:
        print('You win!')
        break
    number = ((max - min) // 2) + min
    print(f"Is integer is {number}? Write 1 if your integer is lower, 2 if integer biggest, 3 if i right")
    token = int(input('Your answer: '))
    if token == 1:
        max = number
    elif token == 2:
        min = number
    elif token == 3:
        user_number = True
        print('Good job')