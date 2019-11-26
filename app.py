# base
import sys
import time
import multiprocessing
import os

# pyqt5 ui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from design import *

from src.CheckFile import checkFunction

class MyApp(QMainWindow, Ui_FileCheck): # 初始化

    def __init__(self, parent=None):

        super(MyApp, self).__init__(parent)
        self.setupUi(self) # 配置ui
    
    def checkFile(self):

        setkeyid = self.keyid.text()
        setcheckid = self.checkid.text().split(";")

        self.changeProgress(50)

        checkFunction(self.basefn, self.checkfn, setkeyid, setcheckid, self.outfn)

        self.changeProgress(100)



    def setBasef(self):
        self.basefn = QFileDialog.getOpenFileName(self)[0]
        self.showbasef.setText(self.basefn)

    def setCheckf(self):
        self.checkfn = QFileDialog.getOpenFileName(self)[0]
        self.showcheckf.setText(self.checkfn)

    def setOutf(self):
        self.outfn = QFileDialog.getExistingDirectory(self)
        self.showoutf.setText(self.outfn)

    def changeProgress(self, num): # 0 =< num <= 100 int 
        self.progressBar.setProperty('value',num)
   

if __name__ == '__main__':

    multiprocessing.freeze_support() # python多进程打包

    app = QApplication(sys.argv)
    MainWin = MyApp()

    MainWin.basef.clicked.connect(MainWin.setBasef)
    MainWin.checkf.clicked.connect(MainWin.setCheckf)
    MainWin.outf.clicked.connect(MainWin.setOutf)
    MainWin.startf.clicked.connect(MainWin.checkFile)

    MainWin.show()
    sys.exit(app.exec_())
