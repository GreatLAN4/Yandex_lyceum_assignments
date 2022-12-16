import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("01.ui", self)
        self.initIU()

    def initIU(self):
        self.btn_calc.clicked.connect(self.Run)

    def Error_print(self):
        self.max_print.setSpecialValueText("!")
        self.min_print.setSpecialValueText("!")
        self.aver_print.setSpecialValueText("!")

    def isDigit(self, lst):
        return all([i.isdigit() for i in lst])

    def Run(self):
        Pass = True
        self.file_name = self.edit_file_name.text()
        try:
            file = open(self.file_name, mode="r", encoding="utf8")
            f_lines = file.readlines()

        except FileNotFoundError:
            self.error_mes.setText(f"file {self.file_name} is not found")
            self.Error_print()
            f_lines = []
            Pass = False

        if Pass and bool(f_lines) is False:
            self.error_mes.setText(f"file {self.file_name} is empty")
            self.Error_print()
            Pass = False

        if Pass:
            f_lines = [b for i in f_lines for b in i.rstrip("\n").split()]

        if not self.isDigit(f_lines):
            self.error_mes.setText(f"file {self.file_name} contains wrong data format")
            self.Error_print()
            Pass = False

        if Pass:
            f_lines = [int(i) for i in f_lines]

            self.max_print.setSpecialValueText(str(max(f_lines)))
            self.min_print.setSpecialValueText(str(min(f_lines)))
            self.aver_print.setSpecialValueText(str(sum(f_lines) / len(f_lines)))

        self.file_name.close()  # если не будет работать закоментить эту строку


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec_())
