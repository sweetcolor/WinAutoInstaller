# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app\view_ui\installer_manager.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1035, 565)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1031, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.installerManagerVerticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.installerManagerVerticalLayout.setObjectName("installerManagerVerticalLayout")
        self.installerLabel = QtWidgets.QLabel(self.layoutWidget)
        self.installerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.installerLabel.setObjectName("installerLabel")
        self.installerManagerVerticalLayout.addWidget(self.installerLabel)
        self.installerButtonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.installerButtonHorizontalLayout.setObjectName("installerButtonHorizontalLayout")
        self.addInstallerPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addInstallerPushButton.setObjectName("addInstallerPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.addInstallerPushButton)
        self.deleteInstallerPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteInstallerPushButton.setObjectName("deleteInstallerPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.deleteInstallerPushButton)
        self.editInstallerPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.editInstallerPushButton.setObjectName("editInstallerPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.editInstallerPushButton)
        self.saveChangesPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveChangesPushButton.setObjectName("saveChangesPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.saveChangesPushButton)
        self.updateInstallerListPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.updateInstallerListPushButton.setObjectName("updateInstallerListPushButton")
        self.installerButtonHorizontalLayout.addWidget(self.updateInstallerListPushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.installerButtonHorizontalLayout.addItem(spacerItem)
        self.installerManagerVerticalLayout.addLayout(self.installerButtonHorizontalLayout)
        self.installerTableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.installerTableWidget.setObjectName("installerTableWidget")
        self.installerTableWidget.setColumnCount(3)
        self.installerTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.installerTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.installerTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.installerTableWidget.setHorizontalHeaderItem(2, item)
        self.installerManagerVerticalLayout.addWidget(self.installerTableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.installerLabel.setText(_translate("Form", "Інсталятори"))
        self.addInstallerPushButton.setText(_translate("Form", "Додати"))
        self.deleteInstallerPushButton.setText(_translate("Form", "Видалити"))
        self.editInstallerPushButton.setText(_translate("Form", "Редагувати"))
        self.saveChangesPushButton.setText(_translate("Form", "Зберегти зміни"))
        self.updateInstallerListPushButton.setText(_translate("Form", "Оновити список"))
        item = self.installerTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Назва"))
        item = self.installerTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Шлях"))
        item = self.installerTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Аргументи"))

