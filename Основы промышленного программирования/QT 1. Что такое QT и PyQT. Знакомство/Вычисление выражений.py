import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLineEdit, QSizePolicy


class Magic(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.Main_LayOut = QHBoxLayout(self)

        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton("->", self)
        self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn.clicked.connect(self.Convert)

        self.input_data = QLineEdit(self)

        self.input_data.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_data = QLineEdit(self)
        self.output_data.setEnabled(False)
        self.output_data.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.Main_LayOut.addWidget(self.input_data)
        self.Main_LayOut.addWidget(self.btn)
        self.Main_LayOut.addWidget(self.output_data)

        self.setLayout(self.Main_LayOut)

    def Convert(self):
        input = str(self.input_data.text())
        print(input)
        output = eval(input)
        self.output_data.setText(str(output))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Magic()
    ex.show()
    sys.exit(app.exec())
