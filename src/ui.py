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
        MainWindow.resize(550, 450)

        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))

        self.layout = QtWidgets.QGridLayout()
        
        self.text_label = QtWidgets.QLabel()
        self.layout.addWidget(self.text_label, 0, 0)

        self.text = QtWidgets.QPlainTextEdit()
        self.layout.addWidget(self.text, 0, 1)
        
        self.link_text_label = QtWidgets.QLabel()
        self.layout.addWidget(self.link_text_label, 1, 0)

        self.link = QtWidgets.QTextEdit()
        self.link.setDisabled(False)
        self.layout.addWidget(self.link, 1, 1)

        self.send = QtWidgets.QPushButton()
        self.send.clicked.connect(self.send_button_pressed)
        self.layout.addWidget(self.send, 2, 1)

        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(0, 5)

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Pastebin GUI")
        self.send.setText("ارسال متن به سرور")
        self.text_label.setText("متن:‌ ")
        self.link_text_label.setText("پیوند:‌ ")
