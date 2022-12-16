import sys
from PyQt5 import uic
from PIL import Image
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsOpacityEffect, QFileDialog

class Transparency(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Управление_прозрачностью.ui", self)
        self.setWindowTitle('Управление прозрачностью')
        self.initUI()


    def initUI(self):
        self.picture = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.picture)
        self.pic.setPixmap(self.pixmap)
        self.pic.resize(500, 500)
        self.transparency.setValue(99)
        self.transparency.valueChanged.connect(self.setTransparency)


    def setTransparency(self, value):
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(value / 100)
        self.pic.setGraphicsEffect(self.opacity_effect)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Transparency()
    ex.show()
    sys.exit(app.exec())