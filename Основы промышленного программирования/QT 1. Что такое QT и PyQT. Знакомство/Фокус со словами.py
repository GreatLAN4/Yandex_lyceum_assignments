import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLineEdit, QVBoxLayout, QSizePolicy


class Magic(QWidget):
    def __init__(self):
        super().__init__()
        self.focus = "Фокус"
        self.arrow = "->"
        self.initUI()

    def initUI(self):
        self.Main_LayOut = QHBoxLayout(self)

        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton(self.arrow, self)
        self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn.clicked.connect(self.Move)

        self.left = QLineEdit(self.focus, self)
        self.left.setEnabled(False)
        self.left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.right = QLineEdit(self)
        self.right.setEnabled(False)
        self.right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.Main_LayOut.addWidget(self.left)
        self.Main_LayOut.addWidget(self.btn)
        self.Main_LayOut.addWidget(self.right)

        self.setLayout(self.Main_LayOut)

    def Move(self):
        if self.arrow == "->":
            self.arrow = "<-"
            self.btn.setText("<-")
            self.right.setText(self.focus)
            self.left.setText("")
        else:
            self.arrow = "->"
            self.btn.setText("->")
            self.left.setText(self.focus)
            self.right.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Magic()
    ex.show()
    sys.exit(app.exec())
