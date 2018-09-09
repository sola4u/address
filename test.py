#/usr/bin/env python
#coding: utf-8

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys
from address import *

class Regist(QWidget):

    def __init__(self):
        super(Regist,self).__init__()
        self.set_ui()

    def set_ui(self):
        self.layout = QVBoxLayout()
        a = Address()
        a.location_label.setText("location_a")
        print(a.location.text())
        b = Address()
        b.location_label.setText("location_b")
        self.commit_bnt = QPushButton('sumbit')
        self.commit_bnt.clicked.connect(self.submit)
        print(b.location.text())
        self.layout.addWidget(a)
        self.layout.addWidget(b)
        self.layout.addWidget(self.commit_bnt)
        self.setLayout(self.layout)
    
    def loc_b(self):
        pass

    def submit(self):
        print(self.location.text())



if __name__ == "__main__":
        app = QApplication(sys.argv)
        mainwindow = Regist()
        mainwindow.show()
        sys.exit(app.exec_())
