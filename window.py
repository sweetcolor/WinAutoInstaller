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
        self.installer_winds_list = list()
        self.installer_wind_components_list = list()
        self.installer_manager = InstallerManager()
        self.network_manager = NetworkManager()
        self.database_manager = DatabaseManager('winautoinstaller')

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
        windows = self.installer_manager.get_program_components()
        for wind_text in windows.keys():
            wind_item = QTreeWidgetItem(self.installerComponentTreeWidget)
            self.installer_winds_list.append(wind_item)
            wind_item.setText(0, wind_text)
            for child_text in windows[wind_text]:
                print(child_text)
                self.installer_wind_components_list.append(QTreeWidgetItem(wind_item))
                self.installer_wind_components_list[-1].setText(0, child_text)

    def open_installer(self):
        installer_path = QFileDialog().getOpenFileName(self.widget, 'Open installer', self._last_dir, '*.exe *.msi')[0]
        if installer_path:
            self.installer_manager.start_installer(installer_path)
            self.refresh_program_list()

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
