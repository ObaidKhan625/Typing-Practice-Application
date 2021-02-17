import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ProgressScreen import QProgressScreen
from PracticeScreen import QDiffGame

class QDiffScreen(QWidget):                         #MAIN SCREEN
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Type Faster")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 0, 900, 600))
        self.label.setPixmap(QPixmap("../Typing Practice Application/images/NINJA-TYPING.png"))
        self.label.setScaledContents(True)
        self.Button1 = QPushButton('\n  Easy  \n', self)
        self.Button1.move(380, 100)
        self.Button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Button2 = QPushButton("\n  Medium  \n", self)
        self.Button2.move(380, 200)
        self.Button3 = QPushButton("\n  Difficult  \n", self)
        self.Button3.move(380, 300)
        self.Button4 = QPushButton("\n  View Progress  \n", self)
        self.Button4.move(380, 400)
        self.Button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_body()

    def main_body(self):                             #MODES
        x = 'Easy'
        self.Button1.clicked.connect(lambda x = x : self.Mode_set('Easy'))
        self.Button2.clicked.connect(lambda x = x : self.Mode_set('Normal'))
        self.Button3.clicked.connect(lambda x = x : self.Mode_set('Difficult'))
        self.Button4.clicked.connect(self.View_Progress)

    def View_Progress(self):
        Prog = QApplication(sys.argv)
        Prog_win = QProgressScreen()
        Prog_win.setGeometry(200, 200, 500, 600)
        Prog_win.show()
        while True:
            Prog.processEvents()

    def Mode_set(self, s):                            #JUMP TO NEW WINDOW FOR MAIN GAME             
        #print(s)
        Main_Game = QApplication(sys.argv)
        Main_Game_win = QDiffGame(s)
        Main_Game_win.show()
        while True:
            Main_Game.processEvents()



def main() :
    Diff = QApplication(sys.argv)
    Diff_win = QDiffScreen()
    Diff_win.setGeometry(200, 200, 900, 600)
    Diff_win.show()
    sys.exit(Diff.exec_())

main()