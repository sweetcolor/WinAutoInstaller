# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app\view_ui\host_manager.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1065, 606)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1063, 604))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.hostListVerticalLayout = QtWidgets.QVBoxLayout()
        self.hostListVerticalLayout.setObjectName("hostListVerticalLayout")
        self.hostListButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.hostListButtonsHorizontalLayout.setObjectName("hostListButtonsHorizontalLayout")
        self.localMachineListLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.localMachineListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.localMachineListLabel.setObjectName("localMachineListLabel")
        self.hostListButtonsHorizontalLayout.addWidget(self.localMachineListLabel)
        self.saveToDatabaselButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveToDatabaselButton.setIcon(icon)
        self.saveToDatabaselButton.setIconSize(QtCore.QSize(27, 27))
        self.saveToDatabaselButton.setCheckable(False)
        self.saveToDatabaselButton.setAutoRepeat(False)
        self.saveToDatabaselButton.setAutoRaise(True)
        self.saveToDatabaselButton.setObjectName("saveToDatabaselButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.saveToDatabaselButton)
        self.fullUpdateHostListButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/full-update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fullUpdateHostListButton.setIcon(icon1)
        self.fullUpdateHostListButton.setIconSize(QtCore.QSize(27, 27))
        self.fullUpdateHostListButton.setCheckable(False)
        self.fullUpdateHostListButton.setAutoRepeat(False)
        self.fullUpdateHostListButton.setAutoRaise(True)
        self.fullUpdateHostListButton.setObjectName("fullUpdateHostListButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.fullUpdateHostListButton)
        self.updateHostListButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateHostListButton.setIcon(icon2)
        self.updateHostListButton.setIconSize(QtCore.QSize(27, 27))
        self.updateHostListButton.setCheckable(False)
        self.updateHostListButton.setAutoRepeat(False)
        self.updateHostListButton.setAutoRaise(True)
        self.updateHostListButton.setObjectName("updateHostListButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.updateHostListButton)
        self.startInstalationOnHostsButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startInstalationOnHostsButton.setIcon(icon3)
        self.startInstalationOnHostsButton.setIconSize(QtCore.QSize(27, 27))
        self.startInstalationOnHostsButton.setCheckable(False)
        self.startInstalationOnHostsButton.setAutoRepeat(False)
        self.startInstalationOnHostsButton.setAutoRaise(True)
        self.startInstalationOnHostsButton.setObjectName("startInstalationOnHostsButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.startInstalationOnHostsButton)
        self.downHostItemButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downHostItemButton.setIcon(icon4)
        self.downHostItemButton.setIconSize(QtCore.QSize(27, 27))
        self.downHostItemButton.setCheckable(False)
        self.downHostItemButton.setAutoRepeat(False)
        self.downHostItemButton.setAutoRaise(True)
        self.downHostItemButton.setObjectName("downHostItemButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.downHostItemButton)
        self.upHostItemButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upHostItemButton.setIcon(icon5)
        self.upHostItemButton.setIconSize(QtCore.QSize(27, 27))
        self.upHostItemButton.setCheckable(False)
        self.upHostItemButton.setAutoRepeat(False)
        self.upHostItemButton.setAutoRaise(True)
        self.upHostItemButton.setObjectName("upHostItemButton")
        self.hostListButtonsHorizontalLayout.addWidget(self.upHostItemButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hostListButtonsHorizontalLayout.addItem(spacerItem)
        self.hostListVerticalLayout.addLayout(self.hostListButtonsHorizontalLayout)
        self.hostListTableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.hostListTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
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
        self.resultLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")
        self.hostListVerticalLayout.addWidget(self.resultLabel)
        self.resutTextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.resutTextEdit.setEnabled(False)
        self.resutTextEdit.setObjectName("resutTextEdit")
        self.hostListVerticalLayout.addWidget(self.resutTextEdit)
        self.verticalLayout.addLayout(self.hostListVerticalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scriptsListVerticalLayout = QtWidgets.QVBoxLayout()
        self.scriptsListVerticalLayout.setObjectName("scriptsListVerticalLayout")
        self.scriptsListButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.scriptsListButtonsHorizontalLayout.setObjectName("scriptsListButtonsHorizontalLayout")
        self.ScriptListLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ScriptListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ScriptListLabel.setObjectName("ScriptListLabel")
        self.scriptsListButtonsHorizontalLayout.addWidget(self.ScriptListLabel)
        self.addNewScriptButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNewScriptButton.setIcon(icon6)
        self.addNewScriptButton.setIconSize(QtCore.QSize(27, 27))
        self.addNewScriptButton.setCheckable(False)
        self.addNewScriptButton.setAutoRepeat(False)
        self.addNewScriptButton.setAutoRaise(True)
        self.addNewScriptButton.setObjectName("addNewScriptButton")
        self.scriptsListButtonsHorizontalLayout.addWidget(self.addNewScriptButton)
        self.removeScriptButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeScriptButton.setIcon(icon7)
        self.removeScriptButton.setIconSize(QtCore.QSize(27, 27))
        self.removeScriptButton.setCheckable(False)
        self.removeScriptButton.setAutoRepeat(False)
        self.removeScriptButton.setAutoRaise(True)
        self.removeScriptButton.setObjectName("removeScriptButton")
        self.scriptsListButtonsHorizontalLayout.addWidget(self.removeScriptButton)
        self.editScriptButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editScriptButton.setIcon(icon8)
        self.editScriptButton.setIconSize(QtCore.QSize(27, 27))
        self.editScriptButton.setCheckable(False)
        self.editScriptButton.setAutoRepeat(False)
        self.editScriptButton.setAutoRaise(True)
        self.editScriptButton.setObjectName("editScriptButton")
        self.scriptsListButtonsHorizontalLayout.addWidget(self.editScriptButton)
        self.updateScriptsListPushButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.updateScriptsListPushButton.setIcon(icon1)
        self.updateScriptsListPushButton.setIconSize(QtCore.QSize(27, 27))
        self.updateScriptsListPushButton.setCheckable(False)
        self.updateScriptsListPushButton.setAutoRepeat(False)
        self.updateScriptsListPushButton.setAutoRaise(True)
        self.updateScriptsListPushButton.setObjectName("updateScriptsListPushButton")
        self.scriptsListButtonsHorizontalLayout.addWidget(self.updateScriptsListPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.scriptsListButtonsHorizontalLayout.addItem(spacerItem1)
        self.scriptsListVerticalLayout.addLayout(self.scriptsListButtonsHorizontalLayout)
        self.scriptListTableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.scriptListTableWidget.setObjectName("scriptListTableWidget")
        self.scriptListTableWidget.setColumnCount(2)
        self.scriptListTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.scriptListTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scriptListTableWidget.setHorizontalHeaderItem(1, item)
        self.scriptsListVerticalLayout.addWidget(self.scriptListTableWidget)
        self.prepareScriptLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.prepareScriptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.prepareScriptLabel.setObjectName("prepareScriptLabel")
        self.scriptsListVerticalLayout.addWidget(self.prepareScriptLabel)
        self.prepareScriptTabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.prepareScriptTabWidget.setObjectName("prepareScriptTabWidget")
        self.currentScriptTab = QtWidgets.QWidget()
        self.currentScriptTab.setObjectName("currentScriptTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.currentScriptTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 511, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.currentScriptVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.currentScriptVerticalLayout.setObjectName("currentScriptVerticalLayout")
        self.currentScriptTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.currentScriptTextEdit.setObjectName("currentScriptTextEdit")
        self.currentScriptVerticalLayout.addWidget(self.currentScriptTextEdit)
        self.verticalLayoutWidget.raise_()
        self.prepareScriptTabWidget.addTab(self.currentScriptTab, "")
        self.allScriptsTab = QtWidgets.QWidget()
        self.allScriptsTab.setObjectName("allScriptsTab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.allScriptsTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 511, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.allScriptsVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.allScriptsVerticalLayout.setObjectName("allScriptsVerticalLayout")
        self.allScriptsTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.allScriptsTextEdit.setObjectName("allScriptsTextEdit")
        self.allScriptsVerticalLayout.addWidget(self.allScriptsTextEdit)
        self.prepareScriptTabWidget.addTab(self.allScriptsTab, "")
        self.scriptsListVerticalLayout.addWidget(self.prepareScriptTabWidget)
        self.gridLayout_2.addLayout(self.scriptsListVerticalLayout, 0, 1, 1, 1)
        self.resultProgressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.resultProgressBar.setEnabled(False)
        self.resultProgressBar.setProperty("value", 0)
        self.resultProgressBar.setObjectName("resultProgressBar")
        self.gridLayout_2.addWidget(self.resultProgressBar, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.prepareScriptTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.localMachineListLabel.setText(_translate("Form", "Список локальних машин"))
        self.saveToDatabaselButton.setToolTip(_translate("Form", "Збереження списку в базі"))
        self.saveToDatabaselButton.setText(_translate("Form", "..."))
        self.fullUpdateHostListButton.setText(_translate("Form", "..."))
        self.updateHostListButton.setToolTip(_translate("Form", "Оновлення"))
        self.updateHostListButton.setText(_translate("Form", "..."))
        self.startInstalationOnHostsButton.setToolTip(_translate("Form", "Запуск"))
        self.startInstalationOnHostsButton.setText(_translate("Form", "..."))
        self.downHostItemButton.setToolTip(_translate("Form", "Осутити вниз"))
        self.downHostItemButton.setText(_translate("Form", "..."))
        self.upHostItemButton.setToolTip(_translate("Form", "Підняти вгори"))
        self.upHostItemButton.setText(_translate("Form", "..."))
        item = self.hostListTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Назва хоста"))
        item = self.hostListTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "IP"))
        item = self.hostListTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Статус"))
        item = self.hostListTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Для запуска"))
        self.resultLabel.setText(_translate("Form", "Результати роботи"))
        self.ScriptListLabel.setText(_translate("Form", "Список сценаріїв"))
        self.addNewScriptButton.setToolTip(_translate("Form", "Додати"))
        self.addNewScriptButton.setText(_translate("Form", "..."))
        self.removeScriptButton.setToolTip(_translate("Form", "Видалити"))
        self.removeScriptButton.setText(_translate("Form", "..."))
        self.editScriptButton.setToolTip(_translate("Form", "Редагувати"))
        self.editScriptButton.setText(_translate("Form", "..."))
        self.updateScriptsListPushButton.setToolTip(_translate("Form", "Оновлення"))
        self.updateScriptsListPushButton.setText(_translate("Form", "..."))
        item = self.scriptListTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Назва сценарія"))
        item = self.scriptListTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Для запуска"))
        self.prepareScriptLabel.setText(_translate("Form", "Підготовка сценаріїв"))
        self.prepareScriptTabWidget.setTabText(self.prepareScriptTabWidget.indexOf(self.currentScriptTab), _translate("Form", "Поточний сценарій"))
        self.prepareScriptTabWidget.setTabText(self.prepareScriptTabWidget.indexOf(self.allScriptsTab), _translate("Form", "Всі сценарії"))

import app.view_py.view_rc
