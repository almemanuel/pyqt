import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = 'First Window'

        self.textbox = QLineEdit(self)
        self.textbox.move(25, 20)
        self.textbox.resize(200, 25)

        football = QPushButton('Football', self)
        football.move(150, 200)
        football.resize(150, 80)
        football.setStyleSheet('''QPushButton {
            background-color: white;
            font: bold;
            font-size: 20px;
            color: black;
            }''')
        football.clicked.connect(self.footballBall)

        basketball = QPushButton('Basketball', self)
        basketball.move(350, 200)
        basketball.resize(150, 80)
        basketball.setStyleSheet('''QPushButton {
            background-color: white;
            font: bold;
            font-size: 20px;
            color: black;
            }''')
        basketball.clicked.connect(self.basketballBall)

        text = QPushButton('Send text', self)
        text.move(550, 200)
        text.resize(150, 80)
        text.setStyleSheet('''QPushButton {
            background-color: white;
            font: bold;
            font-size: 20px;
            color: black;
            }''')
        text.clicked.connect(self.showText)

        self.answer = QLabel(self)
        self.answer.setText("Your Favorite Sport")
        self.answer.move(50, 50)
        self.answer.setStyleSheet('''QLabel {
            font: bold;
            font-size: 25px;
            color: white;
        }''')
        self.answer.resize(400, 50)

        self.boxlabel = QLabel(self)
        self.boxlabel.move(450, 50)
        self.boxlabel.setStyleSheet('''QLabel {
            font: bold;
            font-size: 25px;
            color: white;
        }''')
        self.boxlabel.resize(400, 50)

        self.ball = QLabel(self)
        self.ball.move(50, 400)
        self.ball.resize(200, 200)

        self.windowLoad()


    def windowLoad(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()


    def clean(self):
        self.boxlabel.setText('')
        self.ball.setPixmap(QtGui.QPixmap('../img/clean.png'))


    def footballBall(self):
        self.clean()
        self.ball.setPixmap(QtGui.QPixmap('../img/football.png'))


    def basketballBall(self):
        self.clean()
        self.ball.setPixmap(QtGui.QPixmap('../img/basketball.png'))


    def showText(self):
        self.clean()
        content = self.textbox.text()
        self.boxlabel.setText(content)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())