from form import Ui_MainWindow
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog, QTableWidgetItem
from application_manager import InstallerManager
from network_manager import NetworkManager
from database_manager import DatabaseManager
import os


class Window(Ui_MainWindow):
    def __init__(self, widget=None):
        super(Window, self).__init__()
        self.widget = widget
        self._last_dir = self._default_last_opened_dir()
        self.tree_widgets_list = []
        self.installer_manager = InstallerManager()
        self.network_manager = NetworkManager()
        self.database_manager = DatabaseManager('winautoinstaller')
        self.refresh_program_list()

    def full_update_host_list(self):
        host_description_list = self.network_manager.get_hosts_list()
        self._update_host_list_table_widget(host_description_list)
        self.database_manager.update_hosts_list(host_description_list)

    def update_host_list(self):
        known_hosts_string = ' '.join([i[0] for i in self.database_manager.get_hosts_list()])
        host_description_list = self.network_manager.get_hosts_list(known_hosts_string)
        self._update_host_list_table_widget(host_description_list)

    def refresh_program_list(self):
        self.tree_widgets_list.clear()
        self.installerComponnentTreeWidget.clear()
        windows = self.installer_manager.get_programs_list()
        for i in windows:
            self.tree_widgets_list.append(QTreeWidgetItem(self.installerComponnentTreeWidget))
            self.tree_widgets_list[-1].setText(0, i)

    def open_installer(self):
        installer_path = QFileDialog().getOpenFileName(self.widget, 'Open installer', self._last_dir, '*.exe *.msi')[0]
        if installer_path:
            self.installer_manager.start_installer(installer_path)

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
