import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

# рисуем лицо крипера
class Widget_Art(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Widget_Art крипера.ui", self)
        self.group_buttons = self.buttonGroup.buttons()
        self.initIU()

    def initIU(self):
        self.setWindowTitle('Widget_Art')

        self.table = [[1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                      [1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
        self.group_buttons = self.Binar(self.group_buttons)
        for k in range(8):
            for m in range(8):
                if self.table[k][m] == 1:
                    self.group_buttons[k][m].setText('🟩')
                else:
                    self.group_buttons[k][m].setText('*')
    def Binar(self, group):
        out = [[], [], [], [], [], [], [], []]
        dm = 0
        for i in range(8):
            for l in range(8):
                out[i].append(group[l + dm])
            dm = dm + 8
        return out


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget_Art()
    ex.show()
    sys.exit(app.exec_())
