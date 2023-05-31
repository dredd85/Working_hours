import calendar
from datetime import date
from calendar import monthrange

try:
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

    add_days = int(input('How many additional work days did You have? '))
    sum_worked_days = len(working_days) + add_days

    add_hours = int(input('How many additional hours did You have? '))

    pay = int(input('What is your pay for hour? '))
    hours = int(input('How many hours You worked per day? '))
    payment = sum_worked_days * pay * hours + add_hours * pay

    print('\n')
    print('You worked for {} hours this month'.format(sum_worked_days * hours))
    print('Your payment for this month is:', payment, 'zł')

except ValueError:
    print('Invalid input. Please enter a valid integer for the inputs.')
