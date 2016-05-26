import os
from PyQt5.QtWidgets import QLineEdit
from app.view_py.create_installer_dialog import Ui_Dialog
from app.controllers.dialog_controller import DialogController
from app.widgets.file_dialog import FileDialog


class CreateInstallerDialogController(DialogController, Ui_Dialog):
    def __init__(self, dialog, name='', path='', argv=''):
        self.setupUi(dialog)
        self.file_dialog = FileDialog(widget=dialog)
        default_argv = [
            '',
            'start /wait <назва інсталятора> /s /sms',
            '"/qb-! REBOOT=ReallySuppress"',
            '/SILENT',
            '/S',
            '/s'
        ]
        self.argComboBox.addItems(default_argv)
        line_edit = QLineEdit()
        line_edit.setPlaceholderText('аргументи для тихого режиму')
        self.argComboBox.setLineEdit(line_edit)

        self.nameLineEdit.setText(name)
        self.pathLineEdit.setText(path)
        self.argComboBox.setCurrentText(argv)
        self.connect_slots()
        super().__init__(dialog)

    def get_results(self):
        if self.dialog.result():
            path = self.pathLineEdit.text()
            name = self.nameLineEdit.text()
            arg = self.argComboBox.currentText()
            return name, path, arg
        return None, None, None

    def get_path(self):
        path = self.file_dialog.get_installer_path()
        path = path[0] if path else None
        if path:
            self.pathLineEdit.setText(path)
            if not self.nameLineEdit.text():
                self.nameLineEdit.setText(os.path.basename(path)[:-4])

    def connect_slots(self):
        self.pathToolButton.clicked.connect(self.get_path)
