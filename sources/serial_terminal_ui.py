# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial_terminal.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend.setGeometry(QtCore.QRect(399, 50, 121, 28))
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.checkBoxSendNewline = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxSendNewline.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.checkBoxSendNewline.setObjectName("checkBoxSendNewline")
        self.textEditSerialIn = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditSerialIn.setGeometry(QtCore.QRect(10, 90, 511, 231))
        self.textEditSerialIn.setObjectName("textEditSerialIn")
        self.textEditSerialOut = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditSerialOut.setGeometry(QtCore.QRect(10, 10, 511, 31))
        self.textEditSerialOut.setObjectName("textEditSerialOut")
        self.pushButtonClearText = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClearText.setGeometry(QtCore.QRect(400, 330, 121, 28))
        self.pushButtonClearText.setObjectName("pushButtonClearText")
        self.labelSerialPort = QtWidgets.QLabel(self.centralwidget)
        self.labelSerialPort.setGeometry(QtCore.QRect(530, 20, 71, 16))
        self.labelSerialPort.setObjectName("labelSerialPort")
        self.comboBoxSerialPort = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSerialPort.setGeometry(QtCore.QRect(600, 10, 151, 31))
        self.comboBoxSerialPort.setObjectName("comboBoxSerialPort")
        self.labelBaudrate = QtWidgets.QLabel(self.centralwidget)
        self.labelBaudrate.setGeometry(QtCore.QRect(530, 60, 71, 16))
        self.labelBaudrate.setObjectName("labelBaudrate")
        self.comboBoxBaudrate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBaudrate.setGeometry(QtCore.QRect(600, 50, 151, 31))
        self.comboBoxBaudrate.setObjectName("comboBoxBaudrate")
        self.pushButtonConnect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonConnect.setGeometry(QtCore.QRect(600, 90, 151, 28))
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.pushButtonDisconnect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDisconnect.setGeometry(QtCore.QRect(600, 130, 151, 28))
        self.pushButtonDisconnect.setObjectName("pushButtonDisconnect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Terminal"))
        self.pushButtonSend.setText(_translate("MainWindow", "Send"))
        self.checkBoxSendNewline.setText(_translate("MainWindow", "Send Newline"))
        self.pushButtonClearText.setText(_translate("MainWindow", "Clear Text"))
        self.labelSerialPort.setText(_translate("MainWindow", "Serial Port"))
        self.labelBaudrate.setText(_translate("MainWindow", "Baudrate"))
        self.pushButtonConnect.setText(_translate("MainWindow", "Connect"))
        self.pushButtonDisconnect.setText(_translate("MainWindow", "Disconnect"))
