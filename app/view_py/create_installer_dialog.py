# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app\view_ui\create_installer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(214, 178)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pathLabel = QtWidgets.QLabel(Dialog)
        self.pathLabel.setObjectName("pathLabel")
        self.verticalLayout.addWidget(self.pathLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLineEdit = QtWidgets.QLineEdit(Dialog)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout.addWidget(self.pathLineEdit)
        self.pathToolButton = QtWidgets.QToolButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pathToolButton.setIcon(icon)
        self.pathToolButton.setAutoRaise(False)
        self.pathToolButton.setObjectName("pathToolButton")
        self.horizontalLayout.addWidget(self.pathToolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.verticalLayout.addWidget(self.nameLineEdit)
        self.argLabel = QtWidgets.QLabel(Dialog)
        self.argLabel.setObjectName("argLabel")
        self.verticalLayout.addWidget(self.argLabel)
        self.argComboBox = QtWidgets.QComboBox(Dialog)
        self.argComboBox.setEditable(True)
        self.argComboBox.setObjectName("argComboBox")
        self.verticalLayout.addWidget(self.argComboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pathLabel.setText(_translate("Dialog", "Шлях"))
        self.pathToolButton.setToolTip(_translate("Dialog", "Відкрити інсталятор"))
        self.pathToolButton.setText(_translate("Dialog", "..."))
        self.nameLabel.setText(_translate("Dialog", "Назва"))
        self.argLabel.setText(_translate("Dialog", "Аргументи"))

import app.view_py.view_rc
