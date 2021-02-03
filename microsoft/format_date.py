from datetime import datetime, timedelta
current_date = datetime.now()
print('Today is : ' + str(current_date))

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))
print('*' * 30)

today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

birthday = input('When is your birthday (dd/mm/yyyy)?')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
