# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installer_manager.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.installerButtonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.installerButtonHorizontalLayout.setObjectName("installerButtonHorizontalLayout")
        self.addInstallerPushButton = QtWidgets.QPushButton(Form)
        self.addInstallerPushButton.setObjectName("addInstallerPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.addInstallerPushButton)
        self.deleteInstallerPushButton = QtWidgets.QPushButton(Form)
        self.deleteInstallerPushButton.setObjectName("deleteInstallerPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.deleteInstallerPushButton)
        self.editInstallerPushButton = QtWidgets.QPushButton(Form)
        self.editInstallerPushButton.setObjectName("editInstallerPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.editInstallerPushButton)
        self.saveChangesPushButton = QtWidgets.QPushButton(Form)
        self.saveChangesPushButton.setObjectName("saveChangesPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.saveChangesPushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.installerButtonHorizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.installerButtonHorizontalLayout)
        self.installerLabel = QtWidgets.QLabel(Form)
        self.installerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.installerLabel.setObjectName("installerLabel")
        self.verticalLayout.addWidget(self.installerLabel)
        self.installerTableWidget = QtWidgets.QTableWidget(Form)
        self.installerTableWidget.setObjectName("installerTableWidget")
        self.installerTableWidget.setColumnCount(3)
        self.installerTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.installerTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.installerTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.installerTableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.installerTableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addInstallerPushButton.setText(_translate("Form", "Додати"))
        self.deleteInstallerPushButton.setText(_translate("Form", "Видалити"))
        self.editInstallerPushButton.setText(_translate("Form", "Редагувати"))
        self.saveChangesPushButton.setText(_translate("Form", "Зберегти зміни"))
        self.installerLabel.setText(_translate("Form", "Інсталятори"))
        item = self.installerTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Назва"))
        item = self.installerTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Шлях"))
        item = self.installerTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Аргументи"))

