import sys
from PyQt5 import uic
from PIL import Image
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

def fifXfif(img):
    im = Image.open(img)

    width, height = im.size
    if 500 and 500 == width and height:
        im.save("croped.jpg")

    else:
        left = width / 2 - 250
        top = height / 2 - 250
        right = left + 500
        bottom = top + 500
        im.crop((left, top, right, bottom)).save("croped.jpg")

class Rotator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.new_img = 'new.jpg'
        self.crop = "croped.jpg"
        self.t = QTransform()

        self.initUI()

    def initUI(self):
        self.pic.resize(500, 500)

        self.setWindowTitle('PIL Rotator & Coloriser')
        self.picture = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        fifXfif(self.picture)
        self.pixmap = QPixmap(self.crop)
        self.pic.setPixmap(self.pixmap)

        self.right.clicked.connect(self.Right)
        self.left.clicked.connect(self.Left)
        self.red.clicked.connect(self.Rcolor)
        self.green.clicked.connect(self.Gcolor)
        self.blue.clicked.connect(self.Bcolor)
        self.all.clicked.connect(self.FullColor)


    def Right(self):
        self.t.rotate(90)
        rotated_pixmap = self.pixmap.transformed(self.t)
        self.pic.setPixmap(rotated_pixmap)

    def Left(self):
        self.t.rotate(-90)
        rotated_pixmap = self.pixmap.transformed(self.t)
        self.pic.setPixmap(rotated_pixmap)

    def Rcolor(self):
        img = Image.open(self.crop)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pic.setPixmap(self.pixmap)

    def Gcolor(self):
        img = Image.open(self.crop)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pic.setPixmap(self.pixmap)

    def Bcolor(self):
        img = Image.open(self.crop)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pic.setPixmap(self.pixmap)

    def FullColor(self):
        self.pixmap = QPixmap(self.crop)
        self.pic.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rotator()
    ex.show()
    sys.exit(app.exec())