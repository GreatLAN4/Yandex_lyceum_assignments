import csv
from sys import stdin

dict_keys = [
    "nomen",
    "definitio",
    "pluma",
    "Russian nomen",
    "familia",
    "Russian nomen familia",
]
plant_article = []

for plant_info in stdin:
    plant_page = {}
    plant_info = plant_info.split("\t")

    for num, key in enumerate(dict_keys):
        plant_page[key] = plant_info[num]
    plant_article.append(plant_page)

with open('plantis.csv', "w", newline='') as csvfile:
    writer = csv.DictWriter(
        csvfile, fieldnames=list(plant_article[0].keys()), delimiter=';', quotechar=';')
    writer.writeheader()

    for d in plant_article:
        writer.writerow(d)
