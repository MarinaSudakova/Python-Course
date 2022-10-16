def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(number):
    return number % 2 == 0

def is_not_even(number):
    return number % 2 != 0

def big(number):
    return number > 4
print(my_filter(numbers, lambda number: number > 4))

