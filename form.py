# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 658)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1041, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.createScriptTab = QtWidgets.QWidget()
        self.createScriptTab.setObjectName("createScriptTab")
        self.layoutWidget = QtWidgets.QWidget(self.createScriptTab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1041, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.createScriptGridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.createScriptGridLayout.setObjectName("createScriptGridLayout")
        self.componentVerticalLayout = QtWidgets.QVBoxLayout()
        self.componentVerticalLayout.setObjectName("componentVerticalLayout")
        self.installerComponentLabel = QtWidgets.QLabel(self.layoutWidget)
        self.installerComponentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.installerComponentLabel.setObjectName("installerComponentLabel")
        self.componentVerticalLayout.addWidget(self.installerComponentLabel)
        self.componentButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.componentButtonsHorizontalLayout.setObjectName("componentButtonsHorizontalLayout")
        self.openInstallerButton = QtWidgets.QPushButton(self.layoutWidget)
        self.openInstallerButton.setObjectName("openInstallerButton")
        self.componentButtonsHorizontalLayout.addWidget(self.openInstallerButton)
        self.refreshListButton = QtWidgets.QPushButton(self.layoutWidget)
        self.refreshListButton.setObjectName("refreshListButton")
        self.componentButtonsHorizontalLayout.addWidget(self.refreshListButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.componentButtonsHorizontalLayout.addItem(spacerItem)
        self.componentVerticalLayout.addLayout(self.componentButtonsHorizontalLayout)
        self.installerComponentTreeWidget = QtWidgets.QTreeWidget(self.layoutWidget)
        self.installerComponentTreeWidget.setObjectName("installerComponentTreeWidget")
        self.installerComponentTreeWidget.headerItem().setText(0, "Компоненти інсталятора")
        self.componentVerticalLayout.addWidget(self.installerComponentTreeWidget)
        self.proprtyComponentLabel = QtWidgets.QLabel(self.layoutWidget)
        self.proprtyComponentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.proprtyComponentLabel.setObjectName("proprtyComponentLabel")
        self.componentVerticalLayout.addWidget(self.proprtyComponentLabel)
        self.proprtyComponentTableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.proprtyComponentTableWidget.setObjectName("proprtyComponentTableWidget")
        self.proprtyComponentTableWidget.setColumnCount(2)
        self.proprtyComponentTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.proprtyComponentTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.proprtyComponentTableWidget.setHorizontalHeaderItem(1, item)
        self.componentVerticalLayout.addWidget(self.proprtyComponentTableWidget)
        self.createScriptGridLayout.addLayout(self.componentVerticalLayout, 0, 0, 1, 1)
        self.ScriptsVerticalLayout = QtWidgets.QVBoxLayout()
        self.ScriptsVerticalLayout.setObjectName("ScriptsVerticalLayout")
        self.scriptLabel = QtWidgets.QLabel(self.layoutWidget)
        self.scriptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scriptLabel.setObjectName("scriptLabel")
        self.ScriptsVerticalLayout.addWidget(self.scriptLabel)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.ScriptsVerticalLayout.addWidget(self.textEdit)
        self.createScriptGridLayout.addLayout(self.ScriptsVerticalLayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.createScriptTab, "")
        self.hostManagerTab = QtWidgets.QWidget()
        self.hostManagerTab.setObjectName("hostManagerTab")
        self.layoutWidget1 = QtWidgets.QWidget(self.hostManagerTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 1031, 571))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.hostManagerTabGridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.hostManagerTabGridLayout.setObjectName("hostManagerTabGridLayout")
        self.hostListVerticalLayout = QtWidgets.QVBoxLayout()
        self.hostListVerticalLayout.setObjectName("hostListVerticalLayout")
        self.localMachineListLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.localMachineListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.localMachineListLabel.setObjectName("localMachineListLabel")
        self.hostListVerticalLayout.addWidget(self.localMachineListLabel)
        self.hostListButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.hostListButtonsHorizontalLayout.setObjectName("hostListButtonsHorizontalLayout")
        self.fullUpdateHostListButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.fullUpdateHostListButton.setObjectName("fullUpdateHostListButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.fullUpdateHostListButton)
        self.updateHostListButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.updateHostListButton.setObjectName("updateHostListButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.updateHostListButton)
        self.startInstalationButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.startInstalationButton.setObjectName("startInstalationButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.startInstalationButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hostListButtonsHorizontalLayout.addItem(spacerItem1)
        self.hostListVerticalLayout.addLayout(self.hostListButtonsHorizontalLayout)
        self.hostListTableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        self.hostListTableWidget.setObjectName("hostListTableWidget")
        self.hostListTableWidget.setColumnCount(4)
        self.hostListTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hostListTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hostListTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hostListTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hostListTableWidget.setHorizontalHeaderItem(3, item)
        self.hostListVerticalLayout.addWidget(self.hostListTableWidget)
        self.hostManagerTabGridLayout.addLayout(self.hostListVerticalLayout, 0, 0, 1, 1)
        self.scriptsListVerticalLayout = QtWidgets.QVBoxLayout()
        self.scriptsListVerticalLayout.setObjectName("scriptsListVerticalLayout")
        self.ScriptListLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.ScriptListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ScriptListLabel.setObjectName("ScriptListLabel")
        self.scriptsListVerticalLayout.addWidget(self.ScriptListLabel)
        self.scriptsListButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.scriptsListButtonsHorizontalLayout.setObjectName("scriptsListButtonsHorizontalLayout")
        self.addNewScriptButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.addNewScriptButton.setObjectName("addNewScriptButton")
        self.scriptsListButtonsHorizontalLayout.addWidget(self.addNewScriptButton)
        self.removeScriptButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.removeScriptButton.setObjectName("removeScriptButton")
        self.scriptsListButtonsHorizontalLayout.addWidget(self.removeScriptButton)
        self.editScriptButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.editScriptButton.setObjectName("editScriptButton")
        self.scriptsListButtonsHorizontalLayout.addWidget(self.editScriptButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.scriptsListButtonsHorizontalLayout.addItem(spacerItem2)
        self.scriptsListVerticalLayout.addLayout(self.scriptsListButtonsHorizontalLayout)
        self.scriptListTableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        self.scriptListTableWidget.setObjectName("scriptListTableWidget")
        self.scriptListTableWidget.setColumnCount(2)
        self.scriptListTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.scriptListTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scriptListTableWidget.setHorizontalHeaderItem(1, item)
        self.scriptsListVerticalLayout.addWidget(self.scriptListTableWidget)
        self.hostManagerTabGridLayout.addLayout(self.scriptsListVerticalLayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.hostManagerTab, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1059, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.proprtyComponentTableWidget)
        MainWindow.setTabOrder(self.proprtyComponentTableWidget, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.updateHostListButton)
        MainWindow.setTabOrder(self.updateHostListButton, self.startInstalationButton)
        MainWindow.setTabOrder(self.startInstalationButton, self.hostListTableWidget)
        MainWindow.setTabOrder(self.hostListTableWidget, self.addNewScriptButton)
        MainWindow.setTabOrder(self.addNewScriptButton, self.removeScriptButton)
        MainWindow.setTabOrder(self.removeScriptButton, self.editScriptButton)
        MainWindow.setTabOrder(self.editScriptButton, self.scriptListTableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.installerComponentLabel.setText(_translate("MainWindow", "Компоненти інсталятора"))
        self.openInstallerButton.setText(_translate("MainWindow", "Open"))
        self.refreshListButton.setText(_translate("MainWindow", "Оновити список"))
        self.proprtyComponentLabel.setText(_translate("MainWindow", "Властивості компонента"))
        item = self.proprtyComponentTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Назва"))
        item = self.proprtyComponentTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Значення"))
        self.scriptLabel.setText(_translate("MainWindow", "Скріпт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createScriptTab), _translate("MainWindow", "Створення сценаріїв"))
        self.localMachineListLabel.setText(_translate("MainWindow", "Список локальних машин"))
        self.fullUpdateHostListButton.setText(_translate("MainWindow", "Повне оновлення"))
        self.updateHostListButton.setText(_translate("MainWindow", "Оновлення"))
        self.startInstalationButton.setText(_translate("MainWindow", "Запуск"))
        item = self.hostListTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Назва хоста"))
        item = self.hostListTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP"))
        item = self.hostListTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.hostListTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Для запуска"))
        self.ScriptListLabel.setText(_translate("MainWindow", "Список сценаріїв"))
        self.addNewScriptButton.setText(_translate("MainWindow", "Додати"))
        self.removeScriptButton.setText(_translate("MainWindow", "Видалити"))
        self.editScriptButton.setText(_translate("MainWindow", "Редагувати"))
        item = self.scriptListTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Назва сценарія"))
        item = self.scriptListTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Для запуска"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hostManagerTab), _translate("MainWindow", "Менеджер локальних машин"))

