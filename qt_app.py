from memo_number import MemoNumber
import sys
from PySide2 import QtWidgets, QtGui, QtCore

font = QtGui.QFont('Arial', 16)

class Page1(QtWidgets.QWidget):
    def __init__(self, memo, func_next_page):
        super().__init__()
        self.memo = memo
        self.func_next_page = func_next_page
        self.initUI()

    def initUI(self):
        self.vbox = QtWidgets.QVBoxLayout()

        button = QtWidgets.QPushButton('next')
        button.setToolTip('Go to next value')
        button.clicked.connect(self.on_click)

        self.label = QtWidgets.QLabel()
        self.label.setText(str(self.memo.get_number()))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(font)

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(button)

        self.setLayout(self.vbox)

    def on_click(self):
        if self.memo.get_mode() == 0:
            self.label.setText(self.memo.get_number())
        else:
            self.func_next_page()


class Page2(QtWidgets.QStackedWidget):
    class QuestionWidget(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            vbox = QtWidgets.QVBoxLayout()
            label = QtWidgets.QLabel("Answer")
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setFont(font)

            hbox = QtWidgets.QHBoxLayout()
            self.inp = QtWidgets.QLineEdit()
            hbox.addWidget(self.inp)
            self.button = QtWidgets.QPushButton("Valider")
            vbox.addWidget(label)
            vbox.addLayout(hbox)
            vbox.addWidget(self.button)
            self.setLayout(vbox)

    class AnswerWidget(QtWidgets.QWidget):
        def __init__(self):
            self.initUI()

        def initUI(self):
            super().__init__()
            vbox = QtWidgets.QVBoxLayout()

            self.label_answer = QtWidgets.QLabel()
            self.label_answer.setFont(font)
            self.label_answer.setAlignment(QtCore.Qt.AlignCenter)

            self.label_real_answer = QtWidgets.QLabel()
            self.label_real_answer.setFont(font)
            self.label_real_answer.setAlignment(QtCore.Qt.AlignCenter)

            self.button = QtWidgets.QPushButton("Next")
            vbox.addWidget(self.label_answer)
            vbox.addWidget(self.label_real_answer)
            vbox.addWidget(self.button)
            self.setLayout(vbox)

    def __init__(self, memo, func_next_page):
        super().__init__()
        self.memo = memo
        self.func_next_page = func_next_page
        self.initUI()

    def initUI(self):
        self.question = self.QuestionWidget()
        self.answer = self.AnswerWidget()
        self.question.button.clicked.connect(self.on_click_check_answer)
        self.answer.button.clicked.connect(self.on_click_next)
        self.addWidget(self.question)
        self.addWidget(self.answer)

    def on_click_check_answer(self):
        val = self.question.inp.text()
        rep = self.memo.check_number(val)
        self.question.inp.setText("")

        self.answer.label_answer.setText(str(rep))
        if not rep:
            real_answer = self.memo.file_number[self.memo.counter_answer - 1]
            self.answer.label_real_answer.setText(real_answer)
        else:
            self.answer.label_real_answer.setText("")
        self.setCurrentIndex(1)  # The answer widget

    def on_click_next(self):
        if self.memo.get_mode() == 2:
            self.func_next_page()
        else:
            self.setCurrentIndex(0)


class Page3(QtWidgets.QWidget):
    def __init__(self, memo):
        super().__init__()
        self.memo = memo
        self.initUI()

    def initUI(self):
        vbox = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(
            f"{self.memo.nb_good_answer} / {self.memo.counter_answer}")
        label.setAlignment(QtCore.Qt.AlignHCenter)
        label.setFont(font)
        vbox.addWidget(label)
        self.setLayout(vbox)


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.memo = MemoNumber(3, 3)
        self.title = 'test'
        self.initUI()

    def initUI(self):
        self.stacked_widget = QtWidgets.QStackedWidget(self)

        self.stack1 = Page1(self.memo, self.next_page)
        self.stack2 = Page2(self.memo, self.next_page)

        self.setWindowTitle(self.title)

        self.stacked_widget.addWidget(self.stack1)
        self.stacked_widget.addWidget(self.stack2)
        self.stacked_widget.setCurrentIndex(0)
        self.resize(300, 300)

        self.stacked_widget.move(self.rect().center() -
                                 self.stacked_widget.rect().center())
        self.show()

    def next_page(self):
        i = self.stacked_widget.currentIndex()
        if i == 1:
            self.stack3 = Page3(self.memo)
            self.stacked_widget.addWidget(self.stack3)

        self.stacked_widget.setCurrentIndex(i + 1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = App()
    sys.exit(app.exec_())
