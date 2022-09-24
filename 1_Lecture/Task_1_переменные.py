# целое число — int
# число с плавающей точкой — float
# логический тип (истина/ложь) — bool 
#  ничего (пустой тип) — None

# Приведение к одному типу
birthday_year = '1998'
print(type(birthday_year))

period = 20
print(type(period))

age = int(birthday_year) + period
print(age)

some_str = birthday_year + str(period)
print(some_str)