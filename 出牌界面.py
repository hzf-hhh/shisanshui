# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '出牌界面.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog6(object):
    def setupUi(self, Dialog6):
        Dialog6.setObjectName("Dialog")
        Dialog6.resize(1228, 785)
        self.label = QtWidgets.QLabel(Dialog6)
        self.label.setGeometry(QtCore.QRect(0, 0, 1228, 785))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Desktop/十三水/QQ图片20191023104311.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog6)
        self.pushButton.setGeometry(QtCore.QRect(270, 470, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog6)
        QtCore.QMetaObject.connectSlotsByName(Dialog6)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "福建十三水-出牌界面"))
        self.pushButton.setText(_translate("Dialog", "出牌"))
