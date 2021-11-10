import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QTimer # 로딩화면 위한 타이머
from PyQt5.QtGui import QMovie  # 로딩화면 gif 위한 모듈
import loading
import email

# form_class = uic.loadUiType("email.ui")[0]
form_class = uic.loadUiType("menu.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
              

        self.setupUi(self)

        self.pushButton_email.clicked.connect(self.emailFunction)
        self.pushButton_news.clicked.connect(self.newsFunction)
        self.pushButton_music.clicked.connect(self.musicFunction)
        self.pushButton_weather.clicked.connect(self.weatherFunction)

        self.loading_screen = loading.LoadingScreen()   # 로딩함수 호출

    def emailFunction(self):
        email.emailWindow(self)
    
    def newsFunction(self):
        print("news")

    def musicFunction(self):
        print("music")

    def weatherFunction(self):
        print("weather")



app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()

app.exec_()
