from random import choice
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Morze(QMainWindow):
    def __init__(self):
        super().__init__()
        self.morze = {'a': '•-', 'b': '-•••', 'c': '-•-•', 'd': '-••', 'e': '•', 'f': '••-•', 'g': '--•', 'h': '••••',
                      'i': '••', 'j': '•---', 'k': '-•-', 'l': '•-••', 'm': '--', 'n': '-•', 'o': '---', 'p': '•--•',
                      'q': '--•-', 'r': '•-•', 's': '•••', 't': '-', 'u': '••-', 'v': '•••-', 'w': '•--', 'x': '-••-',
                      'y': '-•--', 'z': '--••'}
        self.output = []

        uic.loadUi("01.ui", self)
        self.initIU()

    def initIU(self):
        self.setWindowTitle('Азбука Морзе 2')

        for key in self.KeyBoard.buttons():
            key.clicked.connect(self.Run)

    def Run(self):
        self.output.append(self.morze.get(self.sender().text()))
        self.encryption.setText("".join(self.output))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Morze()
    ex.show()
    sys.exit(app.exec_())
