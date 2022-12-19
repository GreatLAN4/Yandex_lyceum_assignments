import csv

prise_list = {}
with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        prise_list[row[0]] = int(row[1])
    prises = list(prise_list.values())
    if map(lambda x: x > 1000, prises):
        print("error")

