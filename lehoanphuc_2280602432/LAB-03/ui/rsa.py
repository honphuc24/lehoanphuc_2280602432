# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 81, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 160, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 310, 47, 13))
        self.label_5.setObjectName("label_5")
        self.txtPlaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPlaintext.setGeometry(QtCore.QRect(110, 160, 331, 71))
        self.txtPlaintext.setObjectName("txtPlaintext")
        self.txtCiphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCiphertext.setGeometry(QtCore.QRect(110, 300, 331, 71))
        self.txtCiphertext.setObjectName("txtCiphertext")
        self.txtInformation = QtWidgets.QTextEdit(self.centralwidget)
        self.txtInformation.setGeometry(QtCore.QRect(580, 160, 321, 71))
        self.txtInformation.setObjectName("txtInformation")
        self.txSignature = QtWidgets.QTextEdit(self.centralwidget)
        self.txSignature.setGeometry(QtCore.QRect(580, 300, 321, 71))
        self.txSignature.setObjectName("txSignature")
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(110, 420, 75, 23))
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(360, 420, 75, 23))
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.btnSign = QtWidgets.QPushButton(self.centralwidget)
        self.btnSign.setGeometry(QtCore.QRect(580, 420, 75, 23))
        self.btnSign.setObjectName("btnSign")
        self.btnVerify = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerify.setGeometry(QtCore.QRect(820, 420, 75, 23))
        self.btnVerify.setObjectName("btnVerify")
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(580, 70, 81, 23))
        self.btnGenerate.setObjectName("btnGenerate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain text:"))
        self.label_3.setText(_translate("MainWindow", "Ciphertext:"))
        self.label_4.setText(_translate("MainWindow", "Information:"))
        self.label_5.setText(_translate("MainWindow", "Signature:"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btnSign.setText(_translate("MainWindow", "Sign"))
        self.btnVerify.setText(_translate("MainWindow", "Verify"))
        self.btnGenerate.setText(_translate("MainWindow", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
