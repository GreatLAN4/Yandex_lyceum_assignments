import csv

bought = []
thousand = 1000
prise_list = {}

with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        prise_list[row[0]] = int(row[1])

prise_list = dict(sorted(prise_list.items(), key=lambda x: x[1]))

Bool = True

for key, value in prise_list.items():
    for _ in range(10):
        if thousand - value >= 0:
            thousand -= value
            bought.append(key)
        else:
            Bool = False
    if not Bool:
        break


print(", ".join(bought) if bought else "error")
