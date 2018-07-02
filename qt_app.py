from memo_number import MemoNumber
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QStackedWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, Qt

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.memo = MemoNumber(10, 10)
        self.title = 'test'
        self.initUI()

    def initUI(self):
        self.stacked_widget = QStackedWidget()
        self.vbox = QVBoxLayout()

        self.setWindowTitle(self.title)

        button = QPushButton('next')
        button.setToolTip('Go to next value')
        button.clicked.connect(self.on_click)

        self.label = QLabel()
        self.label.setText(str(self.memo.get_number()))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 16))

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(button)

        self.stacked_widget.addWidget(self.vbox)
        self.setLayout(self.stacked_widget)
        self.show()

    @pyqtSlot()
    def on_click(self):
        if self.memo.get_mode() == 0:
            self.label.setText(self.memo.get_number())
        else:
            self.vbox.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
