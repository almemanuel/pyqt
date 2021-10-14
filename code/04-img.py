import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = 'First Window'

        button1 = QPushButton('Football', self)
        button1.move(150, 200)
        button1.resize(150, 80)
        button1.setStyleSheet('''QPushButton {
            background-color: white;
            font: bold;
            font-size: 20px;
            color: black;
            }''')
        button1.clicked.connect(self.button_click1)

        button2 = QPushButton('Basketball', self)
        button2.move(350, 200)
        button2.resize(150, 80)
        button2.setStyleSheet('''QPushButton {
            background-color: white;
            font: bold;
            font-size: 20px;
            color: black;
            }''')
        button2.clicked.connect(self.button_click2)

        self.label1 = QLabel(self)
        self.label1.setText('Hello, world!')
        self.label1.move(50, 50)
        self.label1.setStyleSheet('''QLabel {
            font: bold;
            font-size: 25px;
            color: white;
        }''')
        self.label1.resize(200, 25)

        self.ball = QLabel(self)
        self.ball.move(50, 400)
        self.ball.resize(200, 200)

        self.windowLoad()


    def windowLoad(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()


    def button_click1(self):
        self.ball.setPixmap(QtGui.QPixmap('../img/football.png'))

    def button_click2(self):
        self.ball.setPixmap(QtGui.QPixmap('../img/basketball.png'))

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())