# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '用户界面.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1228, 785)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1228, 785))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Desktop/十三水/三分天下.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 520, 123, 28))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 520, 123, 28))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 520, 123, 28))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(520,610, 123, 28))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.setStyleSheet("background:transparent;color : #0055ff")
        self.pushButton_2.setStyleSheet("background:transparent;color : #00aa00")
        self.pushButton_3.setStyleSheet("background:transparent;color : #ff0000")
        self.pushButton_4.setStyleSheet("background:transparent;color : #0055ff")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "福建十三水-用户界面"))
        self.pushButton.setText(_translate("Dialog", " 排行榜"))
        self.pushButton_2.setText(_translate("Dialog", "历史纪录"))
        self.pushButton_3.setText(_translate("Dialog", "当前战局"))
        self.pushButton_4.setText(_translate("Dialog", "注销"))
