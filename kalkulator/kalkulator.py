import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("kalkulator")
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.display = QLCDNumber(self)
        vbox.addWidget(self.display)
        self.display.setFixedSize(420,100)
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()
        vbox.addLayout(self.row1)
        vbox.addLayout(self.row2)
        vbox.addLayout(self.row3)
        vbox.addLayout(self.row4)
        self.one = QPushButton("1")
        self.two = QPushButton("2")
        self.three = QPushButton("3")
        self.four = QPushButton("4")
        self.five = QPushButton("5")
        self.six = QPushButton("6")
        self.seven = QPushButton("7")
        self.eight = QPushButton("8")
        self.nine = QPushButton("9")
        self.zero = QPushButton("0")
        self.equals = QPushButton("=")
        self.delete = QPushButton("<-")
        self.sum = QPushButton("+")
        self.minus = QPushButton("-")
        self.multiply = QPushButton("*")
        self.divide = QPushButton("/")
        self.row1.addWidget(self.seven)
        self.row1.addWidget(self.eight)
        self.row1.addWidget(self.nine)
        self.row1.addWidget(self.divide)
        self.row2.addWidget(self.four)
        self.row2.addWidget(self.five)
        self.row2.addWidget(self.six)
        self.row2.addWidget(self.multiply)
        self.row3.addWidget(self.one)
        self.row3.addWidget(self.two)
        self.row3.addWidget(self.three)
        self.row3.addWidget(self.minus)
        self.row4.addWidget(self.equals)
        self.row4.addWidget(self.zero)
        self.row4.addWidget(self.delete)
        self.row4.addWidget(self.sum)
        self.one.setFixedSize(100,65)
        self.two.setFixedSize(100,65)
        self.three.setFixedSize(100,65)
        self.four.setFixedSize(100,65)
        self.five.setFixedSize(100,65)
        self.six.setFixedSize(100,65)
        self.seven.setFixedSize(100,65)
        self.eight.setFixedSize(100,65)
        self.nine.setFixedSize(100,65)
        self.zero.setFixedSize(100,65)
        self.equals.setFixedSize(100,65)
        self.delete.setFixedSize(100,65)
        self.sum.setFixedSize(100,65)
        self.minus.setFixedSize(100,65)
        self.multiply.setFixedSize(100,65)
        self.divide.setFixedSize(100,65)

        
    def button_click(self):
        clicked_button = self.sender()
        clicked_text = clicked_button.text()
        if clicked_text == '=':
            result = str(eval(self.current_input))
            self.display.display(float(result))
            self.current_input = result
        else:
            self.current_input += clicked_text
            self.display.display(float(self.current_input))
            



app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(440,410)
window.show()

app.exec()