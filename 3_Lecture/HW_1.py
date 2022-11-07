# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
#  Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def error_text(what: str):
    try:
        name = (input('Введите {}: '.format(what)))
        if not name:
            raise ValueError
    except ValueError:
        print('Это не текст. Попробуйте снова')
        return error_text(what)
    if not name.isdigit():
        return name
    else:
        print('Вы ввели число. Попробуйте снова')
        return error_text(what)

def error_year():
    try:
        phone = (input(f'Введите возраст: '))
    except ValueError:
        print('Попробуйте снова')
        return error_year()
    if phone.isdigit():
        return phone
    else:
        print('Попробуйте снова')
        return error_year()

n, y, l = error_text('имя'), error_year(), error_text('город проживания')
print(f'{n}, {y} год(а), проживает в городе {l}')