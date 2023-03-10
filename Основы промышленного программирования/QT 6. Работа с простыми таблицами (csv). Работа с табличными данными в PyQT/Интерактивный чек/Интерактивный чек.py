import sys, csv
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.Qt import QHeaderView



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

    def FullFill(self):
        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            next(reader)
            for index, row in enumerate(reader):
                self.prise_list[row[0]] = int(row[1])
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget.setRowCount(len(self.prise_list))

        [self.tableWidget.setItem(n, 0, QTableWidgetItem(item))
         for n, item in enumerate(self.prise_list)]

        [self.tableWidget.setItem(n, 1, QTableWidgetItem(str(item)))
         for n, item in enumerate(self.prise_list.values())]
        [self.tableWidget.setItem(n, 2, QTableWidgetItem("0"))
         for n in range(len(self.prise_list))]


    def UpDate(self):
        try:
            total = sum([int(self.tableWidget.item(i, 1).text()) * int(self.tableWidget.item(i, 2).text())
                         for i in range(len(self.prise_list))])
        except Exception:
            total = "Error"

        self.bill.setText(str(total))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Bill()
    ex.show()
    sys.exit(app.exec())
