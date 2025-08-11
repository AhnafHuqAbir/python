from datetime import date, time, datetime 

today = datetime.today()
print(today)

curent_time = datetime.now()
print(curent_time)

print(f'month: {today.month}')
print(f'year: {today.year}')
print(f'day: {today.day}')

print(time(12, 35, 30))

import calendar
print(calendar.calendar(theyear=2011))
print(calendar.month(2024, 12))