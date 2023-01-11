import math
import sys
from random import sample, randint
from PyQt5.QtGui import QPainter, QColor, QPainterPath, QPolygon
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.left, self.space, self.right = "", "", ""
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

    def mouseMoveEvent(self, event):
        self.setMouseTracking(True)
        self.x, self.y = event.x(), event.y()

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
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        color = (sample(range(0, 256), 3))
        color = QColor(color[0], color[1], color[2])
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
            points = QPolygon([QPoint(self.x - r, self.y - r),
                               QPoint(self.x, self.y + r),
                               QPoint(self.x + r, self.y - r), ])
            qp.drawPolygon(points)
            self.space = False
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
