import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QTimer # 로딩화면 위한 타이머
from PyQt5.QtGui import QMovie  # 로딩화면 gif 위한 모듈

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(510, 340) # 로딩창의 사이즈
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)

        self.movie = QMovie('bg.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(3000, self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()