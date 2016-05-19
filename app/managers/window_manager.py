import os
import itertools

from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

from widgets.file_dialog import FileDialog

from lib.thread_decorator import thread
from app.managers.database_manager import DatabaseManager
from app.managers.installer_script_manager import InstallerScriptManager
from app.managers.menu_manager import MenuManager
from app.managers.network_manager import NetworkManager
from app.view.mainwindow import Ui_MainWindow
# from app.view.form import Ui_MainWindow
from widgets.installerTreeWidgetItem import InstallerTreeWidgetItem


class Window(Ui_MainWindow):
    def __init__(self, widget=None):
        super(Window, self).__init__()
        self.widget = widget
        self._last_dir = self._default_last_opened_dir()
        self.installer_winds_list = list()
        self.installer_wind_components_list = list()
        self.installer_manager = InstallerScriptManager()
        self.network_manager = NetworkManager()
        self.database_manager = DatabaseManager('winautoinstaller')
        self.components = dict()
        self.update_installer_list()
        self.update_scripts_list()
        self.update_host_list()

    # ================
    # createScriptTab
    def run_installer(self):
        installer_path = self.get_installer_path()[0]
        if installer_path:
            self.installer_manager.start_installer(installer_path)
            self.refresh_program_list()

    def refresh_program_list(self):
        self.installer_wind_components_list.clear()
        self.installerComponentTreeWidget.clear()
        components_text, components = self.installer_manager.get_program_components()
        self._refresh_program_list_helper(self.installerComponentTreeWidget, components)

    def _refresh_program_list_helper(self, parent, components):
        for text in components.keys():
            wind_item = InstallerTreeWidgetItem(components[text]['component'], parent)
            wind_item.setText(0, text)
            if components[text]['child']:
                self._refresh_program_list_helper(wind_item, components[text]['child'])

    def clicked_on_program_component(self, index):
        inst_tree_widget_item = self.installerComponentTreeWidget.itemFromIndex(index)
        inst_tree_widget_item.get_installer_component().highlight_control()

    def context_menu_of_program_component(self, event):
        clicked_item_model_index = self.installerComponentTreeWidget.indexAt(event)
        clicked_item_index = self.installerComponentTreeWidget.itemFromIndex(clicked_item_model_index)
        item = clicked_item_index.get_installer_component()
        context_menu = MenuManager(item, self.widget)
        for action in item.get_actions():
            context_menu.addAction(action)
        context_menu.exec(self.widget.mapToGlobal(event))
        self.refresh_program_list()

    # ===============
    # hostManagerTab
    @thread
    def full_update_host_list(self):
        host_description_list = self.network_manager.get_hosts_list()
        self._update_host_list_table_widget(host_description_list)
        self.database_manager.update_hosts_list(host_description_list)

    @thread
    def update_host_list(self):
        known_hosts_string = ' '.join([i[0] for i in self.database_manager.get_hosts_list()])
        host_description_list = self.network_manager.get_hosts_list(known_hosts_string)
        self._update_host_list_table_widget(host_description_list)

    def update_scripts_list(self):
        items = self.database_manager.get_scripts()
        self.scriptListTableWidget.setRowCount(len(items))
        for i, row in enumerate(items):
            for j, column_text in enumerate(row):
                item = QTableWidgetItem(column_text)
                self.scriptListTableWidget.setItem(i, j, item)
            check_box_item = QTableWidgetItem()
            check_box_item.setCheckState(Qt.Checked)
            self.scriptListTableWidget.setItem(i, len(row), check_box_item)

    def start_installation_on_host(self):
        hosts = self._get_checked_hosts()
        installers = self.database_manager.get_installers()
        self.network_manager.run_installers_on_hosts(hosts, installers)

    def _get_checked_hosts(self):
        return [self.hostListTableWidget.item(i, 1).text() for i in range(self.hostListTableWidget.rowCount()) if
                self.hostListTableWidget.item(i, 3).checkState() == Qt.Checked]

    # ===============
    # installerManagerTab
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
                table_item = QTableWidgetItem('/s')
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

    def get_installer_path(self):
        dialog = FileDialog()
        dialog.setFileMode(FileDialog.ExistingFiles)
        open_files = dialog.getOpenFileName(self.widget, 'Open installer', self._last_dir,
                                            '*.exe;;*.msi;;All files (*.*)')
        self._last_dir = os.path.dirname(open_files[0])
        return list(filter(bool, open_files))

    def _update_host_list_table_widget(self, host_description_list):
        self.hostListTableWidget.setRowCount(len(host_description_list))
        for i, host_desc in enumerate(host_description_list):
            for j, desc in enumerate(host_desc):
                table_item = QTableWidgetItem(desc)
                self.hostListTableWidget.setItem(i, j, table_item)
            check_box_item = QTableWidgetItem()
            check_box_item.setCheckState(Qt.Unchecked)
            self.hostListTableWidget.setItem(i, len(host_desc), check_box_item)

    @staticmethod
    def _default_last_opened_dir():
        return os.path.join(os.getcwd(), 'test', 'test_installer')


__author__ = 'Администратор'
