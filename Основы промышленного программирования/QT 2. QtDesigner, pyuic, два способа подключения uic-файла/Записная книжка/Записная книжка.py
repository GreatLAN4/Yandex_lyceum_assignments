import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class NoteBook(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Записная книжка.ui", self)
        self.initIU()

    def initIU(self):
        self.setWindowTitle('Записная книжка')
        self.btn_add.clicked.connect(self.Add)

    def Add(self):
        self.person = f"{self.line_name.text()} {self.line_phone.text()}"
        self.list_person.addItem(self.person)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteBook()
    ex.show()
    sys.exit(app.exec_())
