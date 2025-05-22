from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QPushButton, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QApplication)

app = QApplication([])

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel("")
        self.inpt = QLineEdit("")
        #1
        self.btnprc = QPushButton("%")
        self.btnC = QPushButton("CE")
        self.btnCE = QPushButton("C")
        self.btndel = QPushButton("del")
        #2
        self.btndiv = QPushButton("1/x")
        self.btnsquare = QPushButton("x cube")
        self.btnsqrroot = QPushButton("square root")
        self.btndev = QPushButton("/")
        #3
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btnumn = QPushButton("*")
        #4
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btnmin = QPushButton("-")
        #5
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btnpl = QPushButton("+")
        #6
        self.btnpm = QPushButton("+/-")
        self.btn0 = QPushButton("0")
        self.btnstr = QPushButton(",")
        self.btneq = QPushButton("=")

        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h6 = QHBoxLayout()
        self.h7 = QHBoxLayout()
        self.h8 = QHBoxLayout()
        self.v1 = QVBoxLayout()

        self.h1.addWidget(self.lbl)
        self.h2.addWidget(self.inpt)

        self.h3.addWidget(self.btnprc)
        self.h3.addWidget(self.btnC)
        self.h3.addWidget(self.btnCE)
        self.h3.addWidget(self.btndel)

        self.h4.addWidget(self.btndiv)
        self.h4.addWidget(self.btnsquare)
        self.h4.addWidget(self.btnsqrroot)
        self.h4.addWidget(self.btndev)

        self.h5.addWidget(self.btn7)
        self.h5.addWidget(self.btn8)
        self.h5.addWidget(self.btn9)
        self.h5.addWidget(self.btnumn)

        self.h6.addWidget(self.btn4)
        self.h6.addWidget(self.btn5)
        self.h6.addWidget(self.btn6)
        self.h6.addWidget(self.btnmin)

        self.h7.addWidget(self.btn1)
        self.h7.addWidget(self.btn2)
        self.h7.addWidget(self.btn3)
        self.h7.addWidget(self.btnpl)

        self.h8.addWidget(self.btnpm)
        self.h8.addWidget(self.btn0)
        self.h8.addWidget(self.btnstr)
        self.h8.addWidget(self.btneq)

        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h4)
        self.v1.addLayout(self.h5)
        self.v1.addLayout(self.h6)
        self.v1.addLayout(self.h7)
        self.v1.addLayout(self.h8)

        self.setLayout(self.v1)
        self.show()

root = window()
app.exec_()






