import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = 'First Window'

        button1 = QPushButton('Button 1', self)
        button1.move(150, 200)
        button1.resize(150, 80)
        button1.setStyleSheet('''QPushButton {
            background-color: white;
            font: bold;
            font-size: 20px;
            color: black;
            }''')
        button1.clicked.connect(self.button_click)

        button2 = QPushButton('Button 2', self)
        button2.move(350, 200)
        button2.resize(150, 80)
        button2.setStyleSheet('''QPushButton {
            background-color: white;
            font: bold;
            font-size: 20px;
            color: black;
            }''')
        button2.clicked.connect(self.button_click)

        self.label1 = QLabel(self)
        self.label1.setText('Hello, world!')
        self.label1.move(50, 50)
        self.label1.setStyleSheet('''QLabel {
            font: bold;
            font-size: 25px;
            color: white;
        }''')
        self.label1.resize(200, 25)

        self.windowLoad()


    def windowLoad(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()


    def button_click(self):
        self.label1.setText("I'm using PyQt!")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())