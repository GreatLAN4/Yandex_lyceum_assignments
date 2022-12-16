from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QApplication, QSlider, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Рост хорошего настроения')

        self.slider = QSlider(self)
        self.slider.move(360, 30)
        self.slider.resize(30, 350)
        self.slider.setInvertedAppearance(True)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.scale(self.slider.value() / 100, self.slider.value() / 100)
        self.draw_smile(qp)
        qp.end()

    def draw_smile(self, qp):
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(30, 30, 200, 200)
        qp.drawEllipse(70, 70, 40, 40)
        qp.drawEllipse(145, 70, 40, 40)
        qp.drawArc(QRectF(80.0, 100.0, 100.0, 90.0), 220 * 16, 100 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
