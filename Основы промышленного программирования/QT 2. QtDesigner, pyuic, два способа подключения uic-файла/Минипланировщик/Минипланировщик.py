import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class NoteBook(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Минипланировщик.ui", self)
        self.initIU()

    def initIU(self):
        self.setWindowTitle('Минипланировщик')
        self.btn.clicked.connect(self.Add)

    def Add(self):
        date = self.calendar.selectedDate().toString("dd-MM-yyyy")
        event = f"{date} {self.timeEdit.text()} {self.edit_event.text()}"
        self.listWidget.addItem(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteBook()
    ex.show()
    sys.exit(app.exec_())
