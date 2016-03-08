import os

from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from app.managers.installer_manager import InstallerManager
from app.managers.network_manager import NetworkManager

from app.managers.database_manager import DatabaseManager
from app.managers.menu_manager import MenuManager
from app.view.form import Ui_MainWindow
from app.view.installerTreeWidgetItem import InstallerTreeWidgetItem


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
        # self.components = components
        # for wind_text in components_text.keys():
        #     wind_item = InstallerTreeWidgetItem(self.installerComponentTreeWidget)
        #     self.installer_winds_list.append(wind_item)
        #     wind_item.setText(0, wind_text)
        #     for child_text in components_text[wind_text]:
        #         self.installer_wind_components_list.append(InstallerTreeWidgetItem(wind_item))
        #         self.installer_wind_components_list[-1].setText(0, child_text)

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
