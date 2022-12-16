import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calc.ui", self)

        self.screen = ''
        self.data = ''

        self.initIU()

    def initIU(self):
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.Run)

        self.btn_clear.clicked.connect(self.clear)

        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.operation)

        self.btn_eq.clicked.connect(self.result)

    def Run(self):
        if self.data and self.data[-1].isdigit():
            self.screen += self.sender().text()
        else:
            self.screen = self.sender().text()
        self.data += self.sender().text()

        self.table.display(int(self.screen))

    def clear(self):
        self.screen = ''
        self.data = ''
        self.table.display(0)

    def operation(self):
        if self.data and self.data[-1].isdigit():
            self.data += self.sender().text()
        elif self.data[-1] in '+-*/':
            self.data = self.data[:-1] + self.sender().text()
        print(self.data)

    def result(self):
        self.screen = str(eval(self.data))
        self.data = str(self.screen)
        self.table.display(float(self.screen))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    ex.show()
    sys.exit(app.exec_())
