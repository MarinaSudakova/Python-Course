# Дана дата в формате dd.mm.yyyy, например: 02.11.2013. 
# Ваша задача — вывести дату в текстовом виде, 
# например: второе ноября 2013 года.

date_dict = {
    '01' : 'Первое', '02' : 'Второе', '03' : 'Третье', '04' : 'Четвертое',
    '05' : 'Пятое', '06' : 'Шестое', '07' : 'Седьмое', '08' : 'Восьмое'
}

month_dict = {
    '01' : 'января', '02' : 'февраля', '03' : 'марта', '04' : 'апреля',
    '05' : 'мая', '06' : 'июня','07' : 'июля', '08' : 'августа', '09' : 'сентября',
    '10' : 'октября', '11' : 'ноября', '12' : 'декабря'
}


today = input('Введите дату: ')

date = today[0:2]
month = today[3:5]
year = today[6:]

print('Сегодня {} {} {} года'.format(date_dict[date], month_dict[month], year))
