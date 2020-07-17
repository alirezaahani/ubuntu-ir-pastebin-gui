# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
scriptDir = os.path.dirname(os.path.realpath(__file__))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 479)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.go = QtWidgets.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(10, 10, 551, 29))
        self.go.setObjectName("go")
        self.go.clicked.connect(self.go_button_pressed)
        self.text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 80, 551, 281))
        self.text.setObjectName("text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 551, 21))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 380, 551, 21))
        self.label_2.setObjectName("label_2")
        self.link = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(10, 410, 551, 41))
        self.link.setObjectName("link")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ubuntu iran unofficial gui for pastebin"))
        self.go.setText(_translate("MainWindow", "برو"))
        self.label.setText(_translate("MainWindow", "متن شما :"))
        self.label_2.setText(_translate("MainWindow", "پیوندی که شما برای نمایش متن خود به دیگر افراد ارسال می‌کنید :"))
