# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.

my_list = [3, 44, 12, 47, 8, 8, 44, 73, 86, 47]

new_my_list = []
for number in my_list:
    if my_list.count(number) == 1:
        new_my_list.append(number)

print(new_my_list)