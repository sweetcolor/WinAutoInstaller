# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app\view_ui\create_script.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1042, 570)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1041, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.createScriptGridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.createScriptGridLayout.setObjectName("createScriptGridLayout")
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.scriptLabel.setText(_translate("Form", "Скріпт"))
        self.installerComponentLabel.setText(_translate("Form", "Компоненти інсталятора"))
        self.openInstallerButton.setText(_translate("Form", "Open"))
        self.refreshListButton.setText(_translate("Form", "Оновити список"))
        self.proprtyComponentLabel.setText(_translate("Form", "Властивості компонента"))
        item = self.proprtyComponentTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Назва"))
        item = self.proprtyComponentTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Значення"))

