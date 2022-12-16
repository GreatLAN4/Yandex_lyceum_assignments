from random import choice
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("01.ui", self)
        self.initIU()

    def initIU(self):
        self.setWindowTitle('Миникалькулятор')
        self.btn.clicked.connect(self.Run)

    def Run(self):
        self.composition.display(eval(str(int(self.number1.text()) + int(self.number2.text()))))
        self.difference.display(eval(str(int(self.number1.text()) - int(self.number2.text()))))
        self.multiply.display(eval(str(int(self.number1.text()) * int(self.number2.text()))))
        try:
            self.quotient.display(eval(str(int(self.number1.text()) / int(self.number2.text()))))

        except ZeroDivisionError:
            self.quotient.display("Error")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    ex.show()
    sys.exit(app.exec_())
