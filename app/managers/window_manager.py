import os

from PyQt5.QtWidgets import QTableWidgetItem
from widgets.file_dialog import FileDialog

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

    def full_update_host_list(self):
        host_description_list = self.network_manager.get_hosts_list()
        self._update_host_list_table_widget(host_description_list)
        self.database_manager.update_hosts_list(host_description_list)

    def update_host_list(self):
        known_hosts_string = ' '.join([i[0] for i in self.database_manager.get_hosts_list()])
        host_description_list = self.network_manager.get_hosts_list(known_hosts_string)
        self._update_host_list_table_widget(host_description_list)

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

    def run_installer(self):
        installer_path = self.get_installer_path()[0]
        if installer_path:
            self.installer_manager.start_installer(installer_path)
            self.refresh_program_list()

    def add_installer(self):
        installers_path = self.get_installer_path()
        if installers_path:
            row_count = self.installerTableWidget.rowCount()
            installers_path = installers_path[:-1]
            self.installerTableWidget.setRowCount(row_count + len(installers_path))
            for idx, installer_path in enumerate(installers_path):
                name = installer_path.split('/')[-1][:-4]
                table_item = QTableWidgetItem(name)
                self.installerTableWidget.setItem(row_count + idx, 0, table_item)
                table_item = QTableWidgetItem(installer_path)
                self.installerTableWidget.setItem(row_count + idx, 1, table_item)
                table_item = QTableWidgetItem('')
                self.installerTableWidget.setItem(row_count + idx, 2, table_item)

    def get_installer_path(self):
        dialog = FileDialog()
        dialog.setFileMode(FileDialog.ExistingFiles)
        return dialog.getOpenFileName(self.widget, 'Open installer', self._last_dir,
                                      '*.exe;;*.msi;;All files (*.*)')

    def _update_host_list_table_widget(self, host_description_list):
        self.hostListTableWidget.setRowCount(len(host_description_list))
        for i, host_desc in enumerate(host_description_list):
            for j, desc in enumerate(host_desc):
                table_item = QTableWidgetItem(desc)
                self.hostListTableWidget.setItem(i, j, table_item)

    def _last_opened_dir(self):
        if self._last_dir is None:
            self._last_dir = self._default_last_opened_dir()

    @staticmethod
    def _default_last_opened_dir():
        # return os.environ['USERPROFILE']
        return os.getcwd()


__author__ = 'Администратор'
