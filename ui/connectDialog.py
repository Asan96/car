# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_connect(object):
    def setupUi(self, dialog_connect):
        dialog_connect.setObjectName("dialog_connect")
        dialog_connect.resize(320, 240)
        dialog_connect.setStyleSheet("background-color:white;")
        self.input_macId = QtWidgets.QLineEdit(dialog_connect)
        self.input_macId.setGeometry(QtCore.QRect(80, 80, 171, 31))
        self.input_macId.setWhatsThis("")
        self.input_macId.setStyleSheet("font-family:\'微软雅黑\';font-size:15px;background-color:#f2f2f2;")
        self.input_macId.setInputMask("")
        self.input_macId.setObjectName("input_macId")
        self.btn_connect = QtWidgets.QPushButton(dialog_connect)
        self.btn_connect.setGeometry(QtCore.QRect(80, 140, 61, 31))
        self.btn_connect.setStyleSheet("border-radius:5px;font-family:\'微软雅黑\';font-size:15px;background-color:#1E9FFF;color:#f8f8f8")
        self.btn_connect.setObjectName("btn_connect")
        self.btn_clear = QtWidgets.QPushButton(dialog_connect)
        self.btn_clear.setGeometry(QtCore.QRect(190, 140, 61, 31))
        self.btn_clear.setStyleSheet("border-radius:5px;font-family:\'微软雅黑\';font-size:15px;background-color:#5FB878;color:#f8f8f8")
        self.btn_clear.setObjectName("btn_clear")
        self.label = QtWidgets.QLabel(dialog_connect)
        self.label.setGeometry(QtCore.QRect(130, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-weight:600;font-size:16px;font-family:\'微软雅黑\';color:#FF5722;")
        self.label.setObjectName("label")

        self.retranslateUi(dialog_connect)
        QtCore.QMetaObject.connectSlotsByName(dialog_connect)

    def retranslateUi(self, dialog_connect):
        _translate = QtCore.QCoreApplication.translate
        dialog_connect.setWindowTitle(_translate("dialog_connect", "设备连接"))
        self.input_macId.setPlaceholderText(_translate("dialog_connect", "请输入设备号"))
        self.btn_connect.setText(_translate("dialog_connect", "连接"))
        self.btn_clear.setText(_translate("dialog_connect", "清空"))
        self.label.setText(_translate("dialog_connect", "设备连接"))
