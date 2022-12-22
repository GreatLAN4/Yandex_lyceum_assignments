import csv

prise_list = []
with open('wares.csv', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    next(reader)
    for row in reader:
        if int(row["Old price"  ]) > int(row["New price"]):
            print(row["Name"])

csvfile.close()
