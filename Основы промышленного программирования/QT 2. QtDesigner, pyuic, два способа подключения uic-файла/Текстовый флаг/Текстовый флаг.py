import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QButtonGroup
from PyQt5 import uic


class Flag(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Текстовый флаг.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Текстовый флаг')

        bg1 = QButtonGroup(self)

        self.Bluy_1.clicked.connect(self.color1)
        self.Bluy_1.setChecked(True)

        self.Red_1.clicked.connect(self.color1)
        self.Green_1.clicked.connect(self.color1)

        bg1.addButton(self.Bluy_1)
        bg1.addButton(self.Red_1)
        bg1.addButton(self.Green_1)

        bg2 = QButtonGroup(self)

        self.Bluy_2.clicked.connect(self.color2)
        self.Bluy_2.setChecked(True)

        self.Red_2.clicked.connect(self.color2)
        self.Green_2.clicked.connect(self.color2)

        bg2.addButton(self.Bluy_2)
        bg2.addButton(self.Red_2)
        bg2.addButton(self.Green_2)

        self.Bluy_3.clicked.connect(self.color3)
        self.Bluy_3.setChecked(True)

        bg3 = QButtonGroup(self)

        self.Red_3.clicked.connect(self.color3)
        self.Green_3.clicked.connect(self.color3)

        bg3.addButton(self.Bluy_3)
        bg3.addButton(self.Red_3)
        bg3.addButton(self.Green_3)

        self.lst = [None, None, None]

        self.pushButton.clicked.connect(self.run)

    def color1(self):
        self.lst[0] = self.sender().text()

    def color2(self):
        self.lst[1] = self.sender().text()

    def color3(self):
        self.lst[2] = self.sender().text()

    def run(self):
        self.Answer.clear()
        self.Answer.setText("Цвета: {}, {} и {}".format(self.lst[0], self.lst[1], self.lst[2]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Flag()
    ex.show()
    sys.exit(app.exec_())
