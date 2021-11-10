import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication

class emailWindow(QDialog):
    def __init__(self, parent): # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(emailWindow, self).__init__(parent)
        uic.loadUi("email.ui", self)
        self.show()

        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,300)
        
        self.loadEmail()
    
    def loadEmail(self):
        email=[{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"}]
        row = 0
        self.tableWidget.setRowCount(len(email))
        for mail in email:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(mail["from"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(mail["Title"]))

            row += 1