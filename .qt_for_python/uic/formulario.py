# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\GABRIEL_LUZ\Documents\BD I\avabd\formulario.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(24)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(19, 55, 59);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(12, 12, 12);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 165, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(12, 12, 12);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 220, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(12, 12, 12);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 280, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(12, 12, 12);")
        self.label_4.setObjectName("label_4")
        self.placa = QtWidgets.QLineEdit(self.centralwidget)
        self.placa.setGeometry(QtCore.QRect(300, 160, 211, 31))
        self.placa.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.placa.setObjectName("placa")
        self.modelo = QtWidgets.QLineEdit(self.centralwidget)
        self.modelo.setGeometry(QtCore.QRect(300, 220, 211, 31))
        self.modelo.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.modelo.setObjectName("modelo")
        self.observacao = QtWidgets.QLineEdit(self.centralwidget)
        self.observacao.setGeometry(QtCore.QRect(300, 280, 211, 121))
        self.observacao.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.observacao.setObjectName("observacao")
        self.carro = QtWidgets.QRadioButton(self.centralwidget)
        self.carro.setGeometry(QtCore.QRect(300, 410, 90, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.carro.setFont(font)
        self.carro.setObjectName("carro")
        self.moto = QtWidgets.QRadioButton(self.centralwidget)
        self.moto.setGeometry(QtCore.QRect(300, 450, 90, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.moto.setFont(font)
        self.moto.setObjectName("moto")
        self.caminhao = QtWidgets.QRadioButton(self.centralwidget)
        self.caminhao.setGeometry(QtCore.QRect(300, 487, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.caminhao.setFont(font)
        self.caminhao.setObjectName("caminhao")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 410, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(12, 12, 12);")
        self.label_5.setObjectName("label_5")
        self.cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.cadastrar.setGeometry(QtCore.QRect(560, 410, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cadastrar.setFont(font)
        self.cadastrar.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"background-color: rgb(53, 117, 255);")
        self.cadastrar.setObjectName("cadastrar")
        self.listar = QtWidgets.QPushButton(self.centralwidget)
        self.listar.setGeometry(QtCore.QRect(560, 490, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listar.setFont(font)
        self.listar.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.listar.setObjectName("listar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 105, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(12, 12, 12);")
        self.label_6.setObjectName("label_6")
        self.entrada = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada.setGeometry(QtCore.QRect(300, 100, 211, 31))
        self.entrada.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.entrada.setObjectName("entrada")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.label.setText(_translate("MainWindow", "OFICINA"))
        self.label_2.setText(_translate("MainWindow", "PLACA"))
        self.label_3.setText(_translate("MainWindow", "MODELO"))
        self.label_4.setText(_translate("MainWindow", "OBSERVAÇÕES"))
        self.carro.setText(_translate("MainWindow", "CARRO"))
        self.moto.setText(_translate("MainWindow", "MOTO"))
        self.caminhao.setText(_translate("MainWindow", "CAMINHÃO"))
        self.label_5.setText(_translate("MainWindow", "CATEGORIA"))
        self.cadastrar.setText(_translate("MainWindow", "CADASTRAR"))
        self.listar.setText(_translate("MainWindow", "LISTAR"))
        self.label_6.setText(_translate("MainWindow", "ENTRADA"))
