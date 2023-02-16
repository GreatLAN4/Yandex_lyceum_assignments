import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor

from PyQt5.QtWidgets import QMainWindow, QApplication



class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.amount, self.radius = 0, 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Интерактивный чек')
        self.Button.clicked.connect(self.CalcCircle)


    def CalcCircle(self):
        amount = randint(1, 5)
        radius = randint(10, 150)
        self.amount, self.radius = amount, radius
        self.repaint()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        color = QColor(255, 255, 0)
        qp.setBrush(color)
        for i in range(self.amount):
            qp.drawEllipse(randint(50, 400), randint(50, 400), self.radius, self.radius)

        qp.end()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
