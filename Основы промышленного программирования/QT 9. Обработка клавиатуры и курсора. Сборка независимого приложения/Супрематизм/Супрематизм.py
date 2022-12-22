import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Paint = False
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')


    def mousePressEvent(self, event):
        self.x, self.y = event.x(), event.x()
        if event.button() == Qt.LeftButton:
            self.Paint, self.mode = True, 0

        elif event.button() == Qt.RightButton:
            self.Paint, self.mode = True, 1

    def Draw(self, qp):
        if self.mode == 0:
            qp.drawEllipse(30, 30, 200, 200)
        elif self.mode == 1:
            qp.drawRect(30, 30, 60, 60)
        elif self.mode == 2:
            qp.drawRect(30, 30, 60, 60)


    def paintEvent(self, event):
        if self.Paint:
            qp = QPainter()
            qp.begin(self)
            self.Draw(qp)
            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())