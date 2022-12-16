import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Перемешивание.ui", self)
        self.file = open("lines.txt", mode="r", encoding="utf8")
        file_lines = self.file.readlines()

        self.even = [i.rstrip("\n") for i in file_lines[::2]]
        self.uneven = [i.rstrip("\n") for i in reversed(file_lines[::-2])]

        self.Even = True
        self.initIU()

    def initIU(self):
        self.button_lines_load.clicked.connect(self.Run)

    def Run(self):
        if self.Even:
            self.lines.clear()
            [self.lines.addItem(i) for i in self.even]
            self.Even = False

        elif not self.Even:
            self.lines.clear()
            [self.lines.addItem(i) for i in self.uneven]
            self.Even = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec_())
