# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app\view_ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 652)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.installerTabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.installerTabWidget.setObjectName("installerTabWidget")
        self.createScriptTab = QtWidgets.QWidget()
        self.createScriptTab.setObjectName("createScriptTab")
        self.installerTabWidget.addTab(self.createScriptTab, "")
        self.hostManagerTab = QtWidgets.QWidget()
        self.hostManagerTab.setObjectName("hostManagerTab")
        self.installerTabWidget.addTab(self.hostManagerTab, "")
        self.installerManagerTab = QtWidgets.QWidget()
        self.installerManagerTab.setObjectName("installerManagerTab")
        self.installerTabWidget.addTab(self.installerManagerTab, "")
        self.verticalLayout.addWidget(self.installerTabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1059, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        self.installerTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.installerTabWidget.setTabText(self.installerTabWidget.indexOf(self.createScriptTab), _translate("MainWindow", "Створення сценаріїв"))
        self.installerTabWidget.setTabText(self.installerTabWidget.indexOf(self.hostManagerTab), _translate("MainWindow", "Менеджер локальних машин"))
        self.installerTabWidget.setTabText(self.installerTabWidget.indexOf(self.installerManagerTab), _translate("MainWindow", "Менеджер інсталяторів"))

import app.view_py.view_rc
