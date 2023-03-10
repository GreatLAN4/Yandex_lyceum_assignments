import csv
import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtGui import QColor


def r_hex():
    r = lambda: randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


class Bill(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.prise_list = {}

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Интерактивный чек')
        self.FullFill()
        self.tableWidget.itemChanged.connect(self.UpDate)
        self.btn.clicked.connect(self.Repaint)

    def FullFill(self):
        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            next(reader)
            for index, row in enumerate(reader):
                self.prise_list[row[0]] = int(row[1])
        # Сортирую от большего к меньшему
        self.prise_list = {k: v for k, v in sorted(self.prise_list.items(), key=lambda item: item[1], reverse=True)}

        # Устанавливаю столько строк в файле сколько есть эелементов в списке
        self.tableWidget.setRowCount(len(self.prise_list))

        # Заполняю 1 столбец названием товаров
        [self.tableWidget.setItem(n, 0, QTableWidgetItem(item))
         for n, item in enumerate(self.prise_list)]

        # 2 столбец ценами
        [self.tableWidget.setItem(n, 1, QTableWidgetItem(str(item)))
         for n, item in enumerate(self.prise_list.values())]

        # третий колтчесво куплинного тавара (там 0)
        [self.tableWidget.setItem(n, 2, QTableWidgetItem("0"))
         for n in range(len(self.prise_list))]

        self.Repaint()

    def UpDate(self):
        # Расчитываю сумму к оплате
        try:
            total = sum([int(self.tableWidget.item(i, 1).text()) * int(self.tableWidget.item(i, 2).text())
                         for i in range(len(self.prise_list))])
        except Exception:
            total = "Error"

        # Показываю сумму
        self.bill.setText(str(total))

    def Repaint(self):
        # Обновляю виджет по ножатию кнопки

        for row in range(5):
            rowColor = QColor(r_hex())

            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                item.setBackground(rowColor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Bill()
    ex.show()
    sys.exit(app.exec())
