import itertools
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from app.controllers.tab_controller import TabController
from app.view_py.installer_manager import Ui_Form
from app.controllers.create_installer_dialog_controller import CreateInstallerDialogController


class InstallerManagerTabController(TabController, Ui_Form):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self.widget)
        self.update_installer_list()
        self.connect_slots()

    def update_installer_list(self):
        items = self.database_manager.get_installers()
        self.installerTableWidget.setRowCount(len(items))
        for i, row in enumerate(items):
            for j, column_text in enumerate(row):
                item = QTableWidgetItem(column_text)
                self.installerTableWidget.setItem(i, j, item)

    def edit_installer(self):
        for item in self.installerTableWidget.selectedItems():
            row = item.row()
            name = self.installerTableWidget.item(row, 0).text()
            path = self.installerTableWidget.item(row, 1).text()
            argv = self.installerTableWidget.item(row, 2).text()
            name, installer_path, argv = CreateInstallerDialogController(QDialog(), name, path, argv).get_results()
            if name and installer_path and argv:
                self._set_row_in_installer_table_widget(name, installer_path, argv, row)

    def add_installer(self):
        name, installer_path, argv = CreateInstallerDialogController(QDialog()).get_results()
        if name and installer_path and argv:
            row_count = self.installerTableWidget.rowCount()
            self._set_row_in_installer_table_widget(name, installer_path, argv, row_count)

    def _set_row_in_installer_table_widget(self, name, path, argv, row):
        if self.installerTableWidget.rowCount() <= row:
            self.installerTableWidget.setRowCount(row + 1)
        table_item = QTableWidgetItem(name)
        self.installerTableWidget.setItem(row, 0, table_item)
        table_item = QTableWidgetItem(path)
        self.installerTableWidget.setItem(row, 1, table_item)
        table_item = QTableWidgetItem(argv)
        self.installerTableWidget.setItem(row, 2, table_item)

    def delete_installer(self):
        for index in self.installerTableWidget.selectedIndexes():
            self.installerTableWidget.removeRow(index.row())

    def save_changes_to_database(self):
        items = [list(itertools.repeat(i, 3)) for i in range(self.installerTableWidget.rowCount())]
        for i in range(self.installerTableWidget.rowCount()):
            for j in range(self.installerTableWidget.columnCount()):
                items[i][j] = self.installerTableWidget.item(i, j).text()
        self.database_manager.insert_scripts(items)

    def connect_slots(self):
        self.addInstallerPushButton.clicked.connect(self.add_installer)
        self.editInstallerPushButton.clicked.connect(self.edit_installer)
        self.deleteInstallerPushButton.clicked.connect(self.delete_installer)
        self.saveChangesPushButton.clicked.connect(self.save_changes_to_database)
        self.updateInstallerListPushButton.clicked.connect(self.update_installer_list)

