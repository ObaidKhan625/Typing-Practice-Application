import sys
import random
import time
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
FINAL_ACCURACY = 0
FINAL_TIME = 0
FINAL_TURNS = 0

class QDiffGame(QWidget):
    def __init__(self, a):
        super().__init__()
        self.mode = a
        self.setGeometry(300, 300, 500, 350)
        self.Write = QLineEdit(self)
        self.Label = QLabel(self)
        self.DLabel = QLabel(self)
        self.Button = QPushButton("Enter", self)
        self.Save = QPushButton("Save Progress", self)
        self.Write.returnPressed.connect(self.ReadInput)
        self.main_body()

    def main_body(self):
                                                                        #LAYOUT SETTINGS
        self.n = 0
        self.avg_time = 0
        self.acc = 1
        self.Dtext1 = "Average time : " + str(self.avg_time) + "         Accuracy : " + str(self.acc)
        self.mistakeLabel = QLabel(self)
        self.mistakeLabel.setText("\nBEGIN\n")
        self.Body = QVBoxLayout()
        self.Body.addWidget(self.Write)
        self.Body.addWidget(self.Label)
        self.Body.addWidget(self.Button)
        self.Body.addWidget(self.mistakeLabel)
        self.Body.addWidget(self.DLabel)
        self.Body.addWidget(self.Save)
        self.setLayout(self.Body)
                                                                        #DIFFICULTY FILES
        if(self.mode == 'Easy'):
            self.limit = 10
            self.f = open("text/Easy.txt", "r")
            given_line = random.randint(0, 19)
        elif(self.mode == 'text/Normal'):
            self.limit = 10
            self.f = open("text/Easy.txt", "r")
            given_line = random.randint(0, 19)
        else:
            self.limit = 5
            self.f = open("text/Hard.txt", "r")
            given_line = random.randint(0, 12)
                                                                        #SETTING INITIAL SENTENCE
        self.lines = self.f.readlines()
        self.line = self.lines[given_line]
        self.Label.setText("\n"+self.line+"\n")
        self.DLabel.setText(self.Dtext1)
        self.Write.setPlaceholderText("Enter the text")
        self.start_time = time.time()
        self.Save.clicked.connect(self.SaveProgress)
        self.Button.clicked.connect(self.ReadInput)

    def ReadInput(self):
                                                                        #ACCEPTING A SENTENCE
        u_i = self.Write.displayText()
        self.n += 1
        #print(self.n)
        mistakes = 0
        a = time.time() - self.start_time
        self.start_time = time.time()                                   #STOP TIMER
        minlen = min(len(u_i), len(self.line))
        for i in range(minlen):
            if u_i[i] != self.line[i]:
                mistakes += 1
            else:
                pass
        self.Write.setText("")
        #print(len(self.line), len(u_i))
                                                                         #CHECKING THE INPUT
        if(len(u_i) == 0):                                               #EMPTY INPUT

            self.mistakeLabel.setText("\nType Something!!!\n")

        elif(mistakes == 0 and len(u_i) == len(self.line) - 1):          #PERFECT ACCURACY

            self.mistakeLabel.setText("\nPerfect Sentence!\n")

            self.avg_time = ((self.n-1)*self.avg_time)/self.n + a/self.n
            self.acc = ((self.n-1)*self.acc)/self.n + 1/self.n

            if(self.acc < 0):                                             #ADJUSTING ACCURACY POINTS
                self.acc = 0
            self.Dtext1 = "Average time : " + str(round(self.avg_time, 2)) + "         Accuracy : " + str(round(self.acc, 2)) + "\n"
            self.DLabel.setText(self.Dtext1)

        elif(len(u_i) == len(self.line) - 1 and mistakes > 0):

            if(mistakes > 4):                                              #ZERO ACCURACY
                self.acc = ((self.n-1)*self.acc)/self.n

            else:                                                          #NON-ZERO ACCURACY
                non_zero = 1 - mistakes/5
                self.acc = ((self.n-1)*self.acc)/self.n + non_zero/self.n

            self.avg_time = ((self.n-1)*self.avg_time)/self.n + a/self.n
            self.mistakeLabel.setText("\nSentence has "+str(mistakes)+" mistakes\n\n")
            self.Dtext1 = "Average time : " + str(round(self.avg_time, 2)) + "         Accuracy : " + str(round(self.acc, 2)) + "\n"
            self.DLabel.setText(self.Dtext1)

        elif(len(u_i) >= len(self.line)):                                   #MORE LENGTH OF INPUT SENTENCE THAN REQUIRED
            self.acc = ((self.n-1)*self.acc)/self.n
            #print(self.acc)
            self.mistakeLabel.setText("\nThe Sentence is too Long!\n"+"\n")
            self.Dtext1 = "Average time : " + str(round(self.avg_time, 2)) + "         Accuracy : " + str(round(self.acc, 2)) + "\n"
            self.DLabel.setText(self.Dtext1)

        else:
            self.acc = ((self.n-1)*self.acc)/self.n
            #print(self.acc)
            self.mistakeLabel.setText("\nThe Sentence is Incomplete!\n"+"\n")
            self.Dtext1 = "Average time : " + str(round(self.avg_time, 2)) + "         Accuracy : " + str(round(self.acc, 2)) + "\n"
            self.DLabel.setText(self.Dtext1)

                                              
        global FINAL_TIME
        FINAL_TIME = self.avg_time
        global FINAL_ACCURACY
        FINAL_ACCURACY = self.acc
        global FINAL_TURNS
        FINAL_TURNS = self.n
        if(self.mode == 'Easy' or self.mode == 'Medium'):                     #CHANGING THE DLABEL
            given_line = random.randint(0, 19)
        else:
            given_line = random.randint(0, 12)
        self.line = self.lines[given_line]
        self.Label.setText("\n"+self.line+"\n")
        #print(FINAL_TIME, FINAL_ACCURACY, FINAL_TURNS)

    def SaveProgress(self):
        File_append = open('text/TYPING_PROGRESS.txt', "r+")
        liN = list()
        liT = list()
        liA = list()
        File_append.write(str(FINAL_TURNS) + " " + str(FINAL_TIME) + " " + str(FINAL_ACCURACY) + " " + self.mode + "\n")
        read = File_append.readlines()

        # ONLY PLOT OF TURNS AND TIME

        for i in range(len(read)):
            liN.append(read[i].split(' ')[0])
        for i in range(len(read)):
            liT.append(read[i].split(' ')[1].split('\n')[0])

        liN.append(FINAL_TURNS)
        liT.append(FINAL_TIME)