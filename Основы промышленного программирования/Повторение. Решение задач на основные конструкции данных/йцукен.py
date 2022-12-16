# import Python's datetime module

import datetime


weekDays = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

date_input = input().split(".")
date_input = [int(i) for i in date_input]
date = datetime.date(date_input[2], date_input[1], date_input[0])

BirthdayWeekDays = weekDays[date.weekday()]

print(BirthdayWeekDays)
