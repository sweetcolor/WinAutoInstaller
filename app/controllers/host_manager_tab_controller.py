from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from app.controllers.tab_controller import TabController
from app.controllers.input_network_range_controller import InputNetworkRange
from app.view_py.host_manager import Ui_Form


class HostManagerTabController(TabController, Ui_Form):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self.widget)
        self.update_scripts_list()
        # self.window_manager.update_host_list()
        self.connect_slots()

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
        installers = self.database_manager.get_installers(self._get_checked_installers())
        self.network_manager.run_installers_on_hosts(hosts, installers)

    def _get_checked_hosts(self):
        return [self.hostListTableWidget.item(i, 1).text() for i in range(self.hostListTableWidget.rowCount()) if
                self.hostListTableWidget.item(i, 3).checkState() == Qt.Checked]

    def _get_checked_installers(self):
        return [self.scriptListTableWidget.item(i, 0).text() for i in range(self.scriptListTableWidget.rowCount()) if
                self.scriptListTableWidget.item(i, 1).checkState() == Qt.Checked]

    def update_host_list_table_widget(self, host_description_list):
        self.hostListTableWidget.setRowCount(len(host_description_list))
        for i, host_desc in enumerate(host_description_list):
            for j, desc in enumerate(host_desc):
                table_item = QTableWidgetItem(desc)
                self.hostListTableWidget.setItem(i, j, table_item)
            check_box_item = QTableWidgetItem()
            check_box_item.setCheckState(Qt.Unchecked)
            self.hostListTableWidget.setItem(i, len(host_desc), check_box_item)

    def connect_slots(self):
        self.fullUpdateHostListButton.clicked.connect(lambda x: self.window_manager.full_update_host_list())
        self.updateHostListButton.clicked.connect(lambda x: print('sdfs'))
        self.startInstalationOnHostsButton.clicked.connect(self.start_installation_on_host)
        self.window_manager.updateHostListTableWidget.connect(self.update_host_list_table_widget, Qt.QueuedConnection)
        # scriptsListVerticalLayout
        self.updateScriptsListPushButton.clicked.connect(self.update_scripts_list)

