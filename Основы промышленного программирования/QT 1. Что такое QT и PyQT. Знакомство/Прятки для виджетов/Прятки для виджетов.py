import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class HideAndSeek(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Прятки для виджетов.ui", self)
        self.initIU()

        self.Hidden1, self.Hidden2 = False, False
        self.Hidden3, self.Hidden4 = False, False

    def initIU(self):
        self.setWindowTitle('Прятки для виджетов')

        self.edit1.clicked.connect(self.Appear1)
        self.edit1.setChecked(True)

        self.edit2.clicked.connect(self.Appear2)
        self.edit2.setChecked(True)

        self.edit3.clicked.connect(self.Appear3)
        self.edit3.setChecked(True)

        self.edit4.clicked.connect(self.Appear4)
        self.edit4.setChecked(True)

    def Appear1(self):
        if self.Hidden1:
            self.country.show()
            self.Hidden1 = False
        else:
            self.country.hide()
            self.Hidden1 = True

    def Appear2(self):

        if self.Hidden2:
            self.age.show()
            self.Hidden2 = False
        else:
            self.age.hide()
            self.Hidden2 = True

    def Appear3(self):

        if self.Hidden3:
            self.language.show()
            self.Hidden3 = False
        else:
            self.language.hide()
            self.Hidden3 = True

    def Appear4(self):

        if self.Hidden4:
            self.model.show()
            self.Hidden4 = False
        else:
            self.model.hide()
            self.Hidden4 = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HideAndSeek()
    ex.show()
    sys.exit(app.exec_())
