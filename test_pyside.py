import sys
from PySide2 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.label = QtWidgets.QLabel("Hello world")
        self.show()

app = QtWidgets.QApplication(sys.argv)

widget = MyWidget()

sys.exit(app.exec_())