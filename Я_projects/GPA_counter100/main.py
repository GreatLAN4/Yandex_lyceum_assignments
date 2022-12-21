from PyQt5 import QtWidgets

from quantity_widget import Ui_Form as quantity_Ui
from row_widget import Ui_Form as row_Ui
from answer_widget import Ui_Form as answer_Ui
from main_widget import Ui_MainWindow
from SumLen import ComplexCounter, SimpleCounter, Deu_convert, Usa_convert


class Logic:
    def __init__(self, numbers):
        self.numbers = numbers

    def countGPA(self):

        try:
            try:
                return ComplexCounter(self.numbers)
            except Exception:
                return SimpleCounter(self.numbers)
        except Exception as e:
            return e


class Final(QtWidgets.QWidget, row_Ui):
    def __init__(self, parent=None):
        super(Final, self).__init__(parent)
        self.setupUi(self)

    def show(self, GPA):
        self.res = MyAnswer()
        self.res.show()
        self.res.setGPA(GPA)


class MyAnswer(QtWidgets.QWidget, answer_Ui):
    def __init__(self, parent=None):
        super(MyAnswer, self).__init__(parent)
        self.setupUi(self)

    def setGPA(self, GPA):
        try:
            self.deu.setText(str(Deu_convert(GPA)))
            self.usa.setText(str(Usa_convert(GPA)))
            self.rus.setText(str(GPA))

        except Exception:
            self.deu.setText(str(GPA))
            self.usa.setText(str(GPA))
            self.rus.setText(str(GPA))


class MyQuantity(QtWidgets.QWidget, quantity_Ui):
    def __init__(self, parent=None):
        super(MyQuantity, self).__init__(parent)
        self.setupUi(self)
        self.Done.clicked.connect(self.onClicked)

    def onClicked(self):
        self.log = Logic([self.le1.text(), self.le2.text(),
                          self.le3.text(), self.le4.text(),
                          self.le5.text()])
        self.asw = Final()
        self.asw.show(self.log.countGPA())


class MyRow(QtWidgets.QWidget, row_Ui):
    def __init__(self, parent=None):
        super(MyRow, self).__init__(parent)
        self.setupUi(self)
        self.Done.clicked.connect(self.onClicked)

    def onClicked(self):
        self.log = Logic(self.row.text())
        self.asw = Final()
        print(self.log.countGPA())
        self.asw.show(self.log.countGPA())


class Main(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.btnQnt.clicked.connect(self.onClicked1)
        self.btnRow.clicked.connect(self.onClicked2)

    def onClicked1(self):
        self.quan = MyQuantity()
        self.quan.show()

    def onClicked2(self):
        self.row = MyRow()
        self.row.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())
