# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledNpYqIq.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(440, 550)
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        # font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.num1 = QPushButton(self.centralwidget)
        self.num1.setObjectName(u"num1")
        self.num1.setGeometry(QRect(80, 290, 61, 61))
        self.num_2 = QPushButton(self.centralwidget)
        self.num_2.setObjectName(u"num_2")
        self.num_2.setGeometry(QRect(160, 290, 61, 61))
        self.num_3 = QPushButton(self.centralwidget)
        self.num_3.setObjectName(u"num_3")
        self.num_3.setGeometry(QRect(240, 290, 61, 61))
        self.num_4 = QPushButton(self.centralwidget)
        self.num_4.setObjectName(u"num_4")
        self.num_4.setGeometry(QRect(80, 210, 61, 61))
        self.num_5 = QPushButton(self.centralwidget)
        self.num_5.setObjectName(u"num_5")
        self.num_5.setGeometry(QRect(160, 210, 61, 61))
        self.num_6 = QPushButton(self.centralwidget)
        self.num_6.setObjectName(u"num_6")
        self.num_6.setGeometry(QRect(240, 210, 61, 61))
        self.num_7 = QPushButton(self.centralwidget)
        self.num_7.setObjectName(u"num_7")
        self.num_7.setGeometry(QRect(80, 130, 61, 61))
        self.num_8 = QPushButton(self.centralwidget)
        self.num_8.setObjectName(u"num_8")
        self.num_8.setGeometry(QRect(160, 130, 61, 61))
        self.num_9 = QPushButton(self.centralwidget)
        self.num_9.setObjectName(u"num_9")
        self.num_9.setGeometry(QRect(240, 130, 61, 61))
        self.num_0 = QPushButton(self.centralwidget)
        self.num_0.setObjectName(u"num_0")
        self.num_0.setGeometry(QRect(80, 370, 141, 61))
        self.conma = QPushButton(self.centralwidget)
        self.conma.setObjectName(u"conma")
        self.conma.setGeometry(QRect(240, 370, 61, 61))
        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(320, 290, 61, 61))
        self.equal = QPushButton(self.centralwidget)
        self.equal.setObjectName(u"equal")
        self.equal.setGeometry(QRect(320, 370, 61, 61))
        self.minus = QPushButton(self.centralwidget)
        self.minus.setObjectName(u"minus")
        self.minus.setGeometry(QRect(320, 210, 61, 61))
        self.multiplication = QPushButton(self.centralwidget)
        self.multiplication.setObjectName(u"multiplication")
        self.multiplication.setGeometry(QRect(320, 130, 61, 61))
        self.division = QPushButton(self.centralwidget)
        self.division.setObjectName(u"division")
        self.division.setGeometry(QRect(320, 60, 61, 61))
        font1 = QFont()
        font1.setPointSize(25)
        self.division.setFont(font1)
        self.persent = QPushButton(self.centralwidget)
        self.persent.setObjectName(u"persent")
        self.persent.setGeometry(QRect(240, 60, 61, 61))
        font2 = QFont()
        font2.setPointSize(20)
        self.persent.setFont(font2)
        self.plus_or_minus = QPushButton(self.centralwidget)
        self.plus_or_minus.setObjectName(u"plus_or_minus")
        self.plus_or_minus.setGeometry(QRect(160, 60, 61, 61))
        self.plus_or_minus.setFont(font2)
        self.clear = QPushButton(self.centralwidget)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(80, 60, 61, 61))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(85, 10, 291, 41))
        self.label.setFont(font1)
        self.label.setTabletTracking(False)
        self.label.setStyleSheet(u"QPushButton {\u3000\n"
"\u3000\u3000background-color: hotpink;\n"
"\u3000\u3000border-radius: 10px;\u3000\u3000\u3000\u3000\n"
"}")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setWordWrap(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 440, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.num1.clicked.connect(lambda: self.handleNumber(1))
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.num1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.num_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.num_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.num_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.num_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.num_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.num_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.num_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.num_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.conma.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.multiplication.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.division.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.persent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.plus_or_minus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.label.setText("")
    # retranslateUi
    
    def handleNumber(self, number):
        self.label.setText(number)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())