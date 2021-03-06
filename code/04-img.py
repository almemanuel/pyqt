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

        self.answer = QLabel(self)
        self.answer.setText("Your Favorite Sport's Ball")
        self.answer.move(50, 50)
        self.answer.setStyleSheet('''QLabel {
            font: bold;
            font-size: 25px;
            color: white;
        }''')
        self.answer.resize(400, 50)

        self.ball = QLabel(self)
        self.ball.move(50, 400)
        self.ball.resize(200, 200)

        self.windowLoad()


    def windowLoad(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()


    def footballBall(self):
        self.ball.setPixmap(QtGui.QPixmap('../img/football.png'))

    def basketballBall(self):
        self.ball.setPixmap(QtGui.QPixmap('../img/basketball.png'))

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())