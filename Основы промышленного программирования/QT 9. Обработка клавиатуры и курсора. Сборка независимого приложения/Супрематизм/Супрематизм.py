import math
import sys
from random import sample, randint
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.left, self.space, self.right = False, False, False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

    def mousePressEvent(self, event):
        self.x, self.y = event.x(), event.y()

        if event.button() == Qt.LeftButton:
            self.left = True

        elif event.button() == Qt.RightButton:
            self.right = True

        self.repaint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.space = True

    def paintEvent(self, event):
        qp = QPainter()
        color = (sample(range(0, 256), 3))
        color = QColor(color[0], color[1], color[2])
        qp.begin(self)
        qp.setBrush(color)
        d = randint(10, 75)
        r = d // 2
        if self.left:
            qp.drawEllipse(self.x - r, self.y - r, d, d)
            self.left = False

        elif self.right:
            qp.drawRect(self.x - r, self.y - r, d, d)
            self.right = False

        elif self.space:
            path = QPainterPath()
            path.lineTo(self.x - r, self.y - r)
            path.lineTo(self.x + r, self.y - r)
            path.lineTo(self.x, self.y + r)
            self.space = False
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
