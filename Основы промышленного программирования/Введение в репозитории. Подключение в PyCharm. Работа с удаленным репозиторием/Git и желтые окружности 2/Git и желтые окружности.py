import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication



class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.prise_list = {}

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Интерактивный чек')
        self.Button.clicked.connect(self.Run)

    def Run(self):
        print("clicked")
    def paintEvent(self, event):
        pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
