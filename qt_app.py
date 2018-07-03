from memo_number import MemoNumber
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QStackedWidget, QLineEdit
from PySide2.QtGui import QIcon, QFont
from PySide2.QtCore import Qt

class Page1(QWidget):
    def __init__(self, memo, func_next_page):
        super().__init__()
        self.memo = memo
        self.func_next_page = func_next_page
        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()

        button = QPushButton('next')
        button.setToolTip('Go to next value')
        button.clicked.connect(self.on_click)

        self.label = QLabel()
        self.label.setText(str(self.memo.get_number()))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 16))

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(button)

        self.setLayout(self.vbox)

    def on_click(self):
        if self.memo.get_mode() == 0:
            self.label.setText(self.memo.get_number())
        else:
            self.func_next_page()

class Page2(QWidget):
    def __init__(self, memo, func_next_page):
        super().__init__()
        self.memo = memo
        self.func_next_page = func_next_page
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        label = QLabel("Answer")
        label.setAlignment(Qt.AlignCenter)

        inp = QLineEdit()
        self.button = QPushButton("Valider")

        vbox.addWidget(label)
        vbox.addWidget(inp)
        vbox.addWidget(self.button)
        self.setLayout(vbox)

class App(QWidget):


    def __init__(self):
        super().__init__()
        self.memo = MemoNumber(10, 10)
        self.title = 'test'
        self.initUI()

    def initUI(self):
        self.stacked_widget = QStackedWidget(self)

        self.stack1 = Page1(self.memo, self.next_page)
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.setWindowTitle(self.title)
     
        self.stacked_widget.addWidget(self.stack1)
        self.stacked_widget.addWidget(self.stack2)
        # self.stacked_widget.addWidget(self.stack3)
        self.stacked_widget.setCurrentIndex(0)
        self.resize(300, 300)

        self.stacked_widget.move(self.rect().center() - self.stacked_widget.rect().center())
        self.show()

    def next_page(self):
        i = self.stacked_widget.currentIndex()
        self.stacked_widget.setCurrentIndex(i + 1)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    memo = MemoNumber(10, 10)
    widget = Page2(memo, None)
    widget.show()
    sys.exit(app.exec_())
