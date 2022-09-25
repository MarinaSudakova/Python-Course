friends = ['Max', 'Leo', 'Kate']

for friend in friends:
    print(friend)

# рандж
numbers = range(10)
print(numbers)
print(type(numbers))
print(list(numbers))

# использование в цикле
for i in range(1, len(friends)+1):
    print(i, ')', friends[i-1])