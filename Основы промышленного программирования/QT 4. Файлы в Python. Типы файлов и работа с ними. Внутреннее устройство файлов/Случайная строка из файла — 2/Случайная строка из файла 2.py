from random import choice
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

file = open('lines.txt', mode='r', encoding='utf8')


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Случайная строка из файла.ui", self)
        self.initIU()
        self.file_lines = file.readlines()

    def initIU(self):
        self.setWindowTitle('Случайная строка из файла')
        self.run.clicked.connect(self.Run)

    def Run(self):
        line = choice(self.file_lines)
        try:
            self.runer.setText(line)

        except IndexError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec_())

file.close()
