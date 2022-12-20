import csv

students = {}
with open('vps.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    next(reader)
    for index, row in enumerate(reader):
        students[row[0]] = row[-2]

present = int(input())

[print(key)
 for key, value in students.items()
 if int(value) >= present]
