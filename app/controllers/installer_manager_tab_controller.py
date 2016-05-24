import itertools
from PyQt5.QtWidgets import QTableWidgetItem
from app.controllers.tab_controller import TabController
from app.view_py.installer_manager import Ui_Form


class InstallerManagerTabController(TabController, Ui_Form):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self.widget)
        self.update_installer_list()
        self.window_manager.update_host_list()
        self.connect_slots()

    def update_installer_list(self):
        items = self.database_manager.get_installers()
        self.installerTableWidget.setRowCount(len(items))
        for i, row in enumerate(items):
            for j, column_text in enumerate(row):
                item = QTableWidgetItem(column_text)
                self.installerTableWidget.setItem(i, j, item)

    def add_installer(self):
        installers_path = self.get_installer_path()[:-1]
        if installers_path:
            row_count = self.installerTableWidget.rowCount()
            for idx, installer_path in enumerate(installers_path):
                self.installerTableWidget.setRowCount(row_count + 1)
                name = installer_path.split('/')[-1][:-4]
                table_item = QTableWidgetItem(name)
                self.installerTableWidget.setItem(row_count + idx, 0, table_item)
                table_item = QTableWidgetItem(installer_path)
                self.installerTableWidget.setItem(row_count + idx, 1, table_item)
                table_item = QTableWidgetItem('/S')
                self.installerTableWidget.setItem(row_count + idx, 2, table_item)

    def delete_installer(self):
        for index in self.installerTableWidget.selectedIndexes():
            self.installerTableWidget.removeRow(index.row())

    def save_changes_in_database(self):
        items = [list(itertools.repeat(i, 3)) for i in range(self.installerTableWidget.rowCount())]
        for i in range(self.installerTableWidget.rowCount()):
            for j in range(self.installerTableWidget.columnCount()):
                items[i][j] = self.installerTableWidget.item(i, j).text()
        self.database_manager.insert_scripts(items)

    def connect_slots(self):
        self.addInstallerPushButton.clicked.connect(self.add_installer)
        self.deleteInstallerPushButton.clicked.connect(self.delete_installer)
        self.saveChangesPushButton.clicked.connect(self.save_changes_in_database)
        self.updateInstallerListPushButton.clicked.connect(self.update_installer_list)

