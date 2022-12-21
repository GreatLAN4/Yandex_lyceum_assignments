from csv import writer, QUOTE_MINIMAL
from sys import stdin
plants = []
for line in stdin:

    if '' == line.rstrip():
        break
    plants.append(line.split("\t"))

with open('plantis.csv', 'w', encoding="utf8", newline='') as csvfile:
    writer = writer(
        csvfile, delimiter=';', quotechar='"', quoting=QUOTE_MINIMAL)
    writer.writerow(["nomen", "definitio", "pluma", "Russian nomen", "familia", "Russian nomen familia"])

    for i in plants:
        plants_zero = []
        for j in i:
            j = j.replace("\n", "")
            plants_zero.append(j)
        writer.writerow(plants_zero)
