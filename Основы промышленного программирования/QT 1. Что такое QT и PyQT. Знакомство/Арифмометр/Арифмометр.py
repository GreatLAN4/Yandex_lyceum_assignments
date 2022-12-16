from random import choice
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Арифмометр.ui", self)
        self.initIU()

    def initIU(self):
        self.setWindowTitle('Арифмометр')
        self.composition.clicked.connect(self.Run)
        self.difference.clicked.connect(self.Run)
        self.multiply.clicked.connect(self.Run)

    def Run(self):
        operation = eval(self.number1.text() + self.sender().text() + self.number2.text())
        self.answer.setText(str(operation))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    ex.show()
    sys.exit(app.exec_())
