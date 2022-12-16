import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Word_2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Текстовый редактор 1.ui", self)
        self.initIU()

    def initIU(self):
        self.btn_new.clicked.connect(self.New)
        self.btn_save.clicked.connect(self.Save)
        self.btn_open.clicked.connect(self.Open)

    def New(self):
        self.line_body.clear()
        self.file_name = self.lineEdit.text()
        self.file = open(self.file_name, mode="w+", encoding="utf8")
        self.file.close()

    def Save(self):
        self.file_name = self.lineEdit.text()

        self.file = open(self.file_name, mode="w+", encoding="utf8")
        self.file.seek(0)
        body_text = self.line_body.toPlainText()
        self.file.write(body_text)
        self.file.close()

    def Open(self):
        self.file_name = self.lineEdit.text()
        self.file = open(self.file_name, mode="r", encoding="utf8")
        self.file_lines = self.file.readlines()

        self.line_body.setPlainText("".join(self.file_lines))
        self.file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Word_2()
    ex.show()
    sys.exit(app.exec_())
