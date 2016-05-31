from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QDialog
from app.controllers.input_network_range_controller import InputNetworkRangeController
from app.controllers.tab_controller import TabController
from app.view_py.host_manager import Ui_Form
from app.controllers.result_installation_controller import ResultInstallationController


class HostManagerTabController(TabController, Ui_Form):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.result_tab_name_dict = dict()
        self.setupUi(self.widget)
        self.update_scripts_list()
        self.update_host_list()
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

    def update_host_list(self, full_update=False):
        self.set_disable_host_manager(True)
        range_address = InputNetworkRangeController(QDialog()).get_network_range() if full_update else None
        if not full_update or range_address:
            self.window_manager.update_host_list(full_update, range_address)
        else:
            self.set_disable_host_manager(False)

    def set_disable_host_manager(self, bool_):
        for idx in range(self.hostListButtonsHorizontalLayout.count()):
            widget = self.hostListButtonsHorizontalLayout.itemAt(idx).widget()
            if widget:
                widget.setDisabled(bool_)
        self.hostListTableWidget.setDisabled(bool_)

    def start_installation_on_host(self):
        hosts = self._get_checked_hosts()
        installers = self._prepare_installers()
        self.create_results_tab(hosts)
        self.network_manager.run_installers_on_hosts(hosts, installers)

    def _prepare_installers(self):
        installers = self.database_manager.get_installers(self._get_checked_installers())
        installers = [(x[0].replace(' ', '_') + x[1][-4:], x[1], x[2]) for x in installers]
        installers_script = {x[0]: 'start /wait ' + x[0] + ' ' + x[2] for x in installers}
        installers_path = {x[0]: x[1] for x in installers}
        installers_name = list(installers_path.keys())
        return {
            'names': installers_name,
            'paths': installers_path,
            'scripts': installers_script
        }

    def create_results_tab(self, hosts):
        self.resultLabel.setDisabled(False)
        self.resultTabWidget.setDisabled(False)
        self.resultTabWidget.clear()
        for idx, host in enumerate(hosts):
            self.result_tab_name_dict[host] = idx
            self.resultTabWidget.addTab(ResultInstallationController(), host)

    def append_to_log_file(self, host, text):
        self.resultTabWidget.widget(self.result_tab_name_dict[host]).resutTextEdit.append(text)

    def update_progress_bar(self, host, percent):
        self.resultTabWidget.widget(self.result_tab_name_dict[host]).resultProgressBar.setValue(percent)

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
            row_check_state = Qt.Checked if host_desc[-1] == 'up' else Qt.Unchecked
            check_box_item.setCheckState(row_check_state)
            self.hostListTableWidget.setItem(i, len(host_desc), check_box_item)
        self.set_disable_host_manager(False)

    def connect_slots(self):
        self.fullUpdateHostListButton.clicked.connect(lambda x: self.update_host_list(True))
        self.updateHostListButton.clicked.connect(lambda x: self.update_host_list(False))
        self.startInstalationOnHostsButton.clicked.connect(self.start_installation_on_host)
        self.window_manager.updateHostListTableWidget.connect(self.update_host_list_table_widget, Qt.QueuedConnection)
        # scriptsListVerticalLayout
        self.updateScriptsListPushButton.clicked.connect(self.update_scripts_list)

        self.network_manager.appendToLogFile.connect(self.append_to_log_file, Qt.QueuedConnection)
        self.network_manager.updateProgressBar.connect(self.update_progress_bar, Qt.QueuedConnection)
