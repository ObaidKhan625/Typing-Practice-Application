from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import math

class QProgressScreen(QWidget):                     #PROGRESS SCREEN
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Review")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 0, 700, 600))
        self.label.setPixmap(QPixmap("../Typing Practice Application/images/ProgressBackground.png"))
        self.label.setScaledContents(True)
        self.Button1 = QPushButton('\n  Speed  \n', self)
        self.Button2 = QPushButton('\n  Accuracy  \n', self)
        self.Button3 = QPushButton('\n Overall Score  \n', self)
        self.Button1.move(260, 50)
        self.Button2.move(260, 240)
        self.Button3.move(260, 430)
        self.Button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_body()

    def main_body(self):
        self.Button1.clicked.connect(lambda  x : self.Mode_set('Speed'))
        self.Button2.clicked.connect(lambda  x : self.Mode_set('Accuracy'))
        self.Button3.clicked.connect(lambda  x : self.Mode_set('Overall Score'))

    def Mode_set(self, x):
        File_append = open('text/TYPING_PROGRESS.txt', "r+")
        li = list()
        index = list()
        read = File_append.readlines()
        #print(read)

        # ONLY PLOT OF TURNS AND TIME

        index = [int(i) for i in range(len(read))]

        for i in range(len(read)):
            mode = read[i].split(' ')[3].split('\n')[0]
            if(x == 'Speed'):
                n = read[i].split(' ')[0]
                t = read[i].split(' ')[1]
                d = 0.75
                if mode == 'Medium': d = 0.85
                elif mode == 'Hard': d = 1.0
                else: d = 0.75
                ans = round(d*float(n)*float(t), 2)
                li.append(ans)
                
            if(x == 'Accuracy'):
                n = read[i].split(' ')[0]
                a = read[i].split(' ')[2]
                d = 0.75
                if mode == 'Medium': d = 0.85
                elif mode == 'Hard': d = 1.0
                else: d = 0.75
                ans = round(d*float(n)*float(a), 2)
                li.append(ans)

            if(x == 'Overall Score'):
                n = read[i].split(' ')[0]
                t = read[i].split(' ')[1]
                a = read[i].split(' ')[2]
                d = 0.75
                if mode == 'Medium': 
                    d = 0.85
                    if(float(t) <= 20): t = '1.0'
                    elif(float(t) <= 25): t = '0.75'
                    else: t = '0.5'
                elif mode == 'Hard':
                    d = 1.0
                    if(float(t) <= 25): t = '1.0'
                    elif(float(t) <= 30): t = '0.75'
                    else: t = '0.5'
                else: 
                    d = 0.75
                    if(float(t) <= 15): t = '1.0'
                    elif(float(t) <= 20): t = '0.75'
                    else: t = '0.5'
                ans = round(d*float(n)*float(a)*float(t), 2)
                li.append(ans)

        #print(index_list)
        #print(li)
        index_list = range(min(index), math.ceil(max(index))+1)
        plt.xticks(index_list)
        plt.plot(index_list, li)
        plt.show()