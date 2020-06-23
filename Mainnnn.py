from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import csv
import random
import Check
import Temp
import HelpWIndow
import faulthandler

paths = ['Puzzles_1.csv', 'Puzzles_2.csv', 'Puzzles_3.csv', 'Puzzles_4.csv', 'Puzzles_5.csv',
         'Puzzles_6.csv', 'Puzzles_7.csv', 'Puzzles_8.csv', 'Puzzles_9.csv', 'Puzzles_10.csv',
         'Puzzles_11.csv']


class Ui_MainWindow(QMainWindow, object):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.once_helped = False
        self.once_played = False
        self.once_solved = False
        self.Help_win = ''
        self.play_win = ''
        self.solv_win = ''

    def pl_clos(self, event):
        if self.play_win.gave == "":
            reply = QtWidgets.QMessageBox.question(self, 'Attention!!!',
                                         "You were about to leave the game. Do you Really Want to Quit?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                MainWindow.show()
                self.play_win.thpl.terminate()
                event.accept()
            else:
                event.ignore()
        else:
            MainWindow.show()
            self.play_win.thpl.terminate()
            event.accept()

    def slv_clos(self, event):
        self.solv_win.thpl.terminate()
        MainWindow.show()
        event.accept()

    def help_close(self, event):
        self.Help_win.mediaPlayer.stop()
        self.Help_win.hide()
        event.accept()
        del(self.Help_win)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 300, 300))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 320, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 320, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.installEventFilter(self)
        self.pushButton_2.installEventFilter(self)
        self.pushButton_3.installEventFilter(self)
        self.pix = QtGui.QPixmap('Page.png')
        self.label.setPixmap(self.pix.scaled(300, 300))
        self.retranslateUi(MainWindow)
        self.Player = QtWidgets.QMainWindow()
        self.Solver = QtWidgets.QMainWindow()
        self.Player.closeEvent = self.pl_clos
        self.Solver.closeEvent = self.slv_clos
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku The Game"))
        # self.label.setText(_translate("MainWindow", "TextLabel"))
        MainWindow.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.pushButton.setText(_translate("MainWindow", "Play!!"))
        self.pushButton_2.setText(_translate("MainWindow", "Solver"))
        self.pushButton_3.setText(_translate("MainWindow", "Help"))

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and object is self.pushButton:
            global paths
            puzzle = []
            path = random.choice(paths)
            file = open(path, newline='')
            reader = csv.reader(file)
            numberr = random.randint(1, 10000)
            for x in range(0, numberr):
                d = next(reader)
                puzzle = [d[1], d[2]]
            self.play_win = Check.Ui_PlayWindow(d[1], d[2])
            self.play_win.setupUi(self.Player)
            self.Player.show()
            MainWindow.close()
        elif event.type() == QtCore.QEvent.MouseButtonPress and object is self.pushButton_2:
            self.solv_win = Temp.Ui_MainWindow()
            self.solv_win.setupUi(self.Solver)
            self.Solver.show()
            MainWindow.close()
        elif event.type() == QtCore.QEvent.MouseButtonPress and object is self.pushButton_3:
            self.Help_win = HelpWIndow.Window()
            self.Help_win.closeEvent = self.help_close
            self.Help_win.init_ui()
            self.Help_win.setLayout(self.Help_win.vboxLayout)
            self.Help_win.open_file()
            self.Help_win.show()

        return super(Ui_MainWindow, self).eventFilter(object, event)


if __name__ == "__main__":
    faulthandler.enable()
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
