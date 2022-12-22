import sys
from random import sample
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QInputDialog


class RandomFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Генерация_случайного_флага.ui", self)
        self.setWindowTitle('Генерация случайного флага')
        self.Paint = False
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.run)

    def run(self):
        self.amount, self.ok_pressed = QInputDialog.getInt(
            self, "Введите количество цветов", "Сколько цветов?",
            3, 1, 17, 1)
        self.Paint = True

    def paintEvent(self, event):
        if self.Paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        y = 30
        for i in range(self.amount):
            color = (sample(range(0, 256), 3))
            color = QColor(color[0], color[1], color[2])
            qp.setBrush(color)
            qp.drawRect(110, y, 120, 30)
            y += 30



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomFlag()
    ex.show()
    sys.exit(app.exec_())
