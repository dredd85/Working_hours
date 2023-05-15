import calendar 
from datetime import date
from calendar import monthrange

today = date.today()
month = today.month
year = today.year

working_days = list()

weekday, number_of_days = calendar.monthrange(year, month)

print('The first day of month is:', calendar.day_name[weekday])
print('This month has:', number_of_days, 'days')

cal = calendar.monthcalendar(year, month)
for weeks in cal:
    work_days = weeks[:5]
    for days in work_days:
        if days > 0:
            working_days.append(days)

print('This month has:', len(working_days), 'working days')
print(calendar.month(year, month))
#added a comment for excercise
add_days = int(input('How many addtitional work days did You have? '))
add_hours = int(input('Did you have any additional hours? '))
sum_worked_days = len(working_days) + add_days

print('You worked',sum_worked_days,'days')

pay = int(input('What is your pay for hour? '))
hours = int(input('How long is your working day? '))

payment = sum_worked_days * pay * hours + add_hours * pay

print('Your payment for this months is:', payment, 'zł')
        




