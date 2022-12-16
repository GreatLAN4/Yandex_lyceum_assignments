import xlsxwriter
from sys import stdin as sys

workbook = xlsxwriter.Workbook('Суммы.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type': 'pie'})

data = []

for line in sys:
    line = line.strip("\n").split()
    line[1] = int(line[1])
    data.append(tuple(line))

for row, (item, price) in enumerate(data):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)


# Строим по нашим данным
chart.add_series({"categories": "=Sheet1!A1:A5",
                  "values": '=Sheet1!B1:B5'})

worksheet.insert_chart('C3', chart)

row += 1
worksheet.write(row, 0, 'Всего')
worksheet.write(row, 1, '=SUM(B1:B3)')

workbook.close()
