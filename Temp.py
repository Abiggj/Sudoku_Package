from multiprocessing.pool import ThreadPool
import time
import SOLVER
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

is_solved = False

class Ui_MainWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

    def setupUi(self, MainWindow):
        self.timcl = Waqtclass()
        self.thpl = ThreadPool()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.Exittt = QtWidgets.QAction(MainWindow)
        self.Resett = QtWidgets.QAction(MainWindow)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.pos_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pos_77 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_97 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_78 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_98 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_89 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_87 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_88 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_99 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_79 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_74 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_94 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_75 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_95 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_86 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_84 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_85 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_96 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_76 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_71 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_91 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_72 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_92 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_83 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_81 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_82 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_93 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_73 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_47 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_67 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_48 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_68 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_59 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_57 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_58 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_69 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_49 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_44 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_64 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_45 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_65 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_56 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_54 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_55 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_66 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_46 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_41 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_61 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_42 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_62 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_53 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_51 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_63 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_52 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_43 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_37 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_38 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_29 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_28 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_39 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_34 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_35 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_36 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_32 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_33 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_31 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.question_original = [self.pos_11, self.pos_12, self.pos_13, self.pos_14, self.pos_15, self.pos_16,
                                  self.pos_17, self.pos_18, self.pos_19, self.pos_21, self.pos_22, self.pos_23,
                                  self.pos_24, self.pos_25, self.pos_26, self.pos_27, self.pos_28, self.pos_29,
                                  self.pos_31, self.pos_32, self.pos_33, self.pos_34, self.pos_35, self.pos_36,
                                  self.pos_37, self.pos_38, self.pos_39, self.pos_41, self.pos_42, self.pos_43,
                                  self.pos_44, self.pos_45, self.pos_46, self.pos_47, self.pos_48, self.pos_49,
                                  self.pos_51, self.pos_52, self.pos_53, self.pos_54, self.pos_55, self.pos_56,
                                  self.pos_57, self.pos_58, self.pos_59, self.pos_61, self.pos_62, self.pos_63,
                                  self.pos_64, self.pos_65, self.pos_66, self.pos_67, self.pos_68, self.pos_69,
                                  self.pos_71, self.pos_72, self.pos_73, self.pos_74, self.pos_75, self.pos_76,
                                  self.pos_77, self.pos_78, self.pos_79, self.pos_81, self.pos_82, self.pos_83,
                                  self.pos_84, self.pos_85, self.pos_86, self.pos_87, self.pos_88, self.pos_89,
                                  self.pos_91, self.pos_92, self.pos_93, self.pos_94, self.pos_95, self.pos_96,
                                  self.pos_97, self.pos_98, self.pos_99]
        self.Intonly = QtGui.QIntValidator(1, 9)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 360)
        self.centralwidget.setObjectName("centralwidget")
        self.pos_12.setGeometry(QtCore.QRect(50, 20, 31, 31))
        self.pos_12.setText("")
        self.pos_12.setObjectName("pos_12")
        self.pos_13.setGeometry(QtCore.QRect(80, 20, 31, 31))
        self.pos_13.setObjectName("pos_13")
        self.pos_21.setGeometry(QtCore.QRect(20, 50, 31, 31))
        self.pos_21.setObjectName("pos_21")
        self.pos_22.setGeometry(QtCore.QRect(50, 50, 31, 31))
        self.pos_22.setObjectName("pos_22")
        self.pos_23.setGeometry(QtCore.QRect(80, 50, 31, 31))
        self.pos_23.setObjectName("pos_23")
        self.pos_31.setGeometry(QtCore.QRect(20, 80, 31, 31))
        self.pos_31.setObjectName("pos_31")
        self.pos_32.setGeometry(QtCore.QRect(50, 80, 31, 31))
        self.pos_32.setObjectName("pos_32")
        self.pos_33.setGeometry(QtCore.QRect(80, 80, 31, 31))
        self.pos_33.setObjectName("pos_33")
        self.pos_16.setGeometry(QtCore.QRect(180, 20, 31, 31))
        self.pos_16.setObjectName("pos_16")
        self.pos_36.setGeometry(QtCore.QRect(180, 80, 31, 31))
        self.pos_36.setObjectName("pos_36")
        self.pos_25.setGeometry(QtCore.QRect(150, 50, 31, 31))
        self.pos_25.setObjectName("pos_25")
        self.pos_24.setGeometry(QtCore.QRect(120, 50, 31, 31))
        self.pos_24.setObjectName("pos_24")
        self.pos_26.setGeometry(QtCore.QRect(180, 50, 31, 31))
        self.pos_26.setObjectName("pos_26")
        self.pos_35.setGeometry(QtCore.QRect(150, 80, 31, 31))
        self.pos_35.setObjectName("pos_35")
        self.pos_15.setGeometry(QtCore.QRect(150, 20, 31, 31))
        self.pos_15.setObjectName("pos_15")
        self.pos_34.setGeometry(QtCore.QRect(120, 80, 31, 31))
        self.pos_34.setObjectName("pos_34")
        self.pos_14.setGeometry(QtCore.QRect(120, 20, 31, 31))
        self.pos_14.setObjectName("pos_14")
        self.pos_19.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pos_19.setObjectName("pos_19")
        self.pos_39.setGeometry(QtCore.QRect(280, 80, 31, 31))
        self.pos_39.setObjectName("pos_39")
        self.pos_28.setGeometry(QtCore.QRect(250, 50, 31, 31))
        self.pos_28.setObjectName("pos_28")
        self.pos_27.setGeometry(QtCore.QRect(220, 50, 31, 31))
        self.pos_27.setObjectName("pos_27")
        self.pos_29.setGeometry(QtCore.QRect(280, 50, 31, 31))
        self.pos_29.setObjectName("pos_29")
        self.pos_38.setGeometry(QtCore.QRect(250, 80, 31, 31))
        self.pos_38.setObjectName("pos_38")
        self.pos_18.setGeometry(QtCore.QRect(250, 20, 31, 31))
        self.pos_18.setObjectName("pos_18")
        self.pos_37.setGeometry(QtCore.QRect(220, 80, 31, 31))
        self.pos_37.setObjectName("pos_37")
        self.pos_17.setGeometry(QtCore.QRect(220, 20, 31, 31))
        self.pos_17.setObjectName("pos_17")
        self.pos_43.setGeometry(QtCore.QRect(80, 120, 31, 31))
        self.pos_43.setObjectName("pos_43")
        self.pos_63.setGeometry(QtCore.QRect(80, 180, 31, 31))
        self.pos_63.setObjectName("pos_63")
        self.pos_52.setGeometry(QtCore.QRect(50, 150, 31, 31))
        self.pos_52.setObjectName("pos_52")
        self.pos_51.setGeometry(QtCore.QRect(20, 150, 31, 31))
        self.pos_51.setObjectName("pos_51")
        self.pos_53.setGeometry(QtCore.QRect(80, 150, 31, 31))
        self.pos_53.setObjectName("pos_53")
        self.pos_62.setGeometry(QtCore.QRect(50, 180, 31, 31))
        self.pos_62.setObjectName("pos_62")
        self.pos_42.setGeometry(QtCore.QRect(50, 120, 31, 31))
        self.pos_42.setObjectName("pos_42")
        self.pos_61.setGeometry(QtCore.QRect(20, 180, 31, 31))
        self.pos_61.setObjectName("pos_61")
        self.pos_41.setGeometry(QtCore.QRect(20, 120, 31, 31))
        self.pos_41.setObjectName("pos_41")
        self.pos_46.setGeometry(QtCore.QRect(180, 120, 31, 31))
        self.pos_46.setObjectName("pos_46")
        self.pos_66.setGeometry(QtCore.QRect(180, 180, 31, 31))
        self.pos_66.setObjectName("pos_66")
        self.pos_55.setGeometry(QtCore.QRect(150, 150, 31, 31))
        self.pos_55.setObjectName("pos_55")
        self.pos_54.setGeometry(QtCore.QRect(120, 150, 31, 31))
        self.pos_54.setObjectName("pos_54")
        self.pos_56.setGeometry(QtCore.QRect(180, 150, 31, 31))
        self.pos_56.setObjectName("pos_56")
        self.pos_65.setGeometry(QtCore.QRect(150, 180, 31, 31))
        self.pos_65.setObjectName("pos_65")
        self.pos_45.setGeometry(QtCore.QRect(150, 120, 31, 31))
        self.pos_45.setObjectName("pos_45")
        self.pos_64.setGeometry(QtCore.QRect(120, 180, 31, 31))
        self.pos_64.setObjectName("pos_64")
        self.pos_44.setGeometry(QtCore.QRect(120, 120, 31, 31))
        self.pos_44.setObjectName("pos_44")
        self.pos_49.setGeometry(QtCore.QRect(280, 120, 31, 31))
        self.pos_49.setObjectName("pos_49")
        self.pos_69.setGeometry(QtCore.QRect(280, 180, 31, 31))
        self.pos_69.setObjectName("pos_69")
        self.pos_58.setGeometry(QtCore.QRect(250, 150, 31, 31))
        self.pos_58.setObjectName("pos_58")
        self.pos_57.setGeometry(QtCore.QRect(220, 150, 31, 31))
        self.pos_57.setObjectName("pos_57")
        self.pos_59.setGeometry(QtCore.QRect(280, 150, 31, 31))
        self.pos_59.setObjectName("pos_59")
        self.pos_68.setGeometry(QtCore.QRect(250, 180, 31, 31))
        self.pos_68.setObjectName("pos_68")
        self.pos_48.setGeometry(QtCore.QRect(250, 120, 31, 31))
        self.pos_48.setObjectName("pos_48")
        self.pos_67.setGeometry(QtCore.QRect(220, 180, 31, 31))
        self.pos_67.setObjectName("pos_67")
        self.pos_47.setGeometry(QtCore.QRect(220, 120, 31, 31))
        self.pos_47.setObjectName("pos_47")
        self.pos_73.setGeometry(QtCore.QRect(80, 220, 31, 31))
        self.pos_73.setObjectName("pos_73")
        self.pos_93.setGeometry(QtCore.QRect(80, 280, 31, 31))
        self.pos_93.setObjectName("pos_93")
        self.pos_82.setGeometry(QtCore.QRect(50, 250, 31, 31))
        self.pos_82.setObjectName("pos_82")
        self.pos_81.setGeometry(QtCore.QRect(20, 250, 31, 31))
        self.pos_81.setObjectName("pos_81")
        self.pos_83.setGeometry(QtCore.QRect(80, 250, 31, 31))
        self.pos_83.setObjectName("pos_83")
        self.pos_92.setGeometry(QtCore.QRect(50, 280, 31, 31))
        self.pos_92.setObjectName("pos_92")
        self.pos_72.setGeometry(QtCore.QRect(50, 220, 31, 31))
        self.pos_72.setObjectName("pos_72")
        self.pos_91.setGeometry(QtCore.QRect(20, 280, 31, 31))
        self.pos_91.setObjectName("pos_91")
        self.pos_71.setGeometry(QtCore.QRect(20, 220, 31, 31))
        self.pos_71.setObjectName("pos_71")
        self.pos_76.setGeometry(QtCore.QRect(180, 220, 31, 31))
        self.pos_76.setObjectName("pos_76")
        self.pos_96.setGeometry(QtCore.QRect(180, 280, 31, 31))
        self.pos_96.setObjectName("pos_96")
        self.pos_85.setGeometry(QtCore.QRect(150, 250, 31, 31))
        self.pos_85.setObjectName("pos_85")
        self.pos_84.setGeometry(QtCore.QRect(120, 250, 31, 31))
        self.pos_84.setObjectName("pos_84")
        self.pos_86.setGeometry(QtCore.QRect(180, 250, 31, 31))
        self.pos_86.setObjectName("pos_86")
        self.pos_95.setGeometry(QtCore.QRect(150, 280, 31, 31))
        self.pos_95.setObjectName("pos_95")
        self.pos_75.setGeometry(QtCore.QRect(150, 220, 31, 31))
        self.pos_75.setObjectName("pos_75")
        self.pos_94.setGeometry(QtCore.QRect(120, 280, 31, 31))
        self.pos_94.setObjectName("pos_94")
        self.pos_74.setGeometry(QtCore.QRect(120, 220, 31, 31))
        self.pos_74.setObjectName("pos_74")
        self.pos_79.setGeometry(QtCore.QRect(280, 220, 31, 31))
        self.pos_79.setObjectName("pos_79")
        self.pos_99.setGeometry(QtCore.QRect(280, 280, 31, 31))
        self.pos_99.setObjectName("pos_99")
        self.pos_88.setGeometry(QtCore.QRect(250, 250, 31, 31))
        self.pos_88.setObjectName("pos_88")
        self.pos_87.setGeometry(QtCore.QRect(220, 250, 31, 31))
        self.pos_87.setObjectName("pos_87")
        self.pos_89.setGeometry(QtCore.QRect(280, 250, 31, 31))
        self.pos_89.setObjectName("pos_89")
        self.pos_98.setGeometry(QtCore.QRect(250, 280, 31, 31))
        self.pos_98.setObjectName("pos_98")
        self.pos_78.setGeometry(QtCore.QRect(250, 220, 31, 31))
        self.pos_78.setObjectName("pos_78")
        self.pos_97.setGeometry(QtCore.QRect(220, 280, 31, 31))
        self.pos_97.setObjectName("pos_97")
        self.pos_77.setGeometry(QtCore.QRect(220, 220, 31, 31))
        self.pos_77.setObjectName("pos_77")
        self.pushButton.setGeometry(QtCore.QRect(340, 20, 89, 31))
        self.pushButton.setObjectName("pushButton")
        self.pos_11.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.pos_11.setObjectName("pos_11")
        self.lcdNumber.setGeometry(QtCore.QRect(330, 230, 111, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit.setObjectName("actionExit")
        self.Exittt.setObjectName("Exittt")
        self.Resett.setObjectName("Reset")
        self.menuMenu.addAction(self.Exittt)
        self.menuMenu.addAction(self.Resett)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        for x in self.question_original:
            x.installEventFilter(self)
            x.setValidator(self.Intonly)
        self.pushButton.installEventFilter(self)
        self.Exittt.triggered.connect(MainWindow.close)
        self.Resett.triggered.connect(self.Reseter)

    def Reseter(self):
        global is_solved
        is_solved = False
        self.pushButton.setEnabled(True)
        self.lcdNumber.display(0)
        for x in self.question_original:
            x.setText("")
            x.setStyleSheet("color: black;")
            x.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solver"))
        self.pushButton.setText(_translate("MainWindow", "SOLVE"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit..."))
        self.Exittt.setText(_translate("MainWindow", "Exit"))
        self.Resett.setText(_translate("MainWindow", "Reset"))

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusIn and obj in self.question_original:
            global is_solved
            if not is_solved:
                obj.clear()

        elif event.type() == QtCore.QEvent.MouseButtonPress and obj is self.pushButton:
            self.molcl = MolveClass(ques_org=self.question_original)
            self.molcl.MOLVE.connect(self.molve)
            self.molcl.btn_cmnd.connect(self.btn_hndl)
            self.timcl.Waqt.connect(self.tim)
            self.thpl.apply_async(self.molcl.run, ())
            self.thpl.apply_async(self.timcl.run, ())
        elif event.type() == QtCore.QEvent.KeyPress and obj in self.question_original:
            ind = self.question_original.index(obj)
            x = ind + 1
            if x >80:
                x = 0
            if self.question_original[x].text() == '':
                self.question_original[x].setFocus()
            else:
                while self.question_original[x].text() != '':
                    x += 1
                    if x >= 80:
                        x = 0
                    if self.question_original[x].text() == '':
                        self.question_original[x].setFocus()
                        break
        return super(Ui_MainWindow, self).eventFilter(obj, event)

    def tim(self,timn):
        self.lcdNumber.display(timn)

    def molve(self):
        global is_solved
        is_solved = True

    def btn_hndl(self, adv):
        if adv == 'able':
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)


class Waqtclass(QtCore.QThread):
    Waqt = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Waqtclass, self).__init__(parent)

    def run(self):
        global is_solved
        timl = 0
        while not is_solved:
            time.sleep(1)
            timl += 1
            minute = int(timl / 60)
            second = timl - (minute * 60)
            timn = '{:02}:{:02}'.format(minute, second)
            self.Waqt.emit(timn)
        is_solved = False


class MolveClass(QtCore.QThread):
    MOLVE = pyqtSignal()
    btn_cmnd = pyqtSignal(str)

    def __init__(self, ques_org, parent=None):
        self.q = ques_org
        super(MolveClass, self).__init__(parent)

    def run(self):
        y = 0
        global is_solved
        question_solveable = dict()
        for x in range(10, 100):
            if x % 10 == 0:
                continue
            else:
                n = self.q[y].text()
                if n == '':
                    question_solveable[x] = 0
                    self.q[y].setStyleSheet("color: blue;")
                    y += 1
                else:
                    question_solveable[x] = int(self.q[y].text())
                    self.q[y].setStyleSheet("color: red;")
                    y += 1
        question_solveable = SOLVER.solverr(question_solveable)
        if question_solveable.possible_check():
            self.btn_cmnd.emit('False')
            question_solveable.solve_please()
            question_solveable = question_solveable.solved_set
            y = 0
            for x in range(10, 100):
                if x % 10 == 0:
                    continue
                elif y < 80:
                    self.q[y].setText(str(question_solveable[x]))
                    self.q[y].setEnabled(False)
                    y += 1
                elif y == 80:
                    self.q[y].setText(str(question_solveable[x]))
                    self.q[y].setEnabled(False)
            self.MOLVE.emit()
        else:
            self.MOLVE.emit()
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Checked!!")
            msg.setText("The given Sudoku problem is not Solveable!!")
            msg.exec_()
            for x in self.q:
                x.setStyleSheet("color: black;")
            self.btn_cmnd.emit('able')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    plainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(plainWindow)
    plainWindow.show()
    sys.exit(app.exec_())