from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal

from app.lib.thread_decorator import thread


class WindowManager(QObject):
    updateHostListTableWidget = pyqtSignal(list, name='updateHostListTableWidget')

    def __init__(self, window_controller):
        self.network_manager = window_controller.network_manager
        self.database_manager = window_controller.database_manager
        super().__init__()

    @thread
    def full_update_host_list(self):
        # range_address = InputNetworkRange(QDialog(self.widget))
        host_description_list = self.network_manager.get_hosts_list()
        self.database_manager.update_hosts_list(host_description_list)
        self.updateHostListTableWidget.emit(host_description_list)

    @thread
    def update_host_list(self):
        known_hosts_string = ' '.join([i[0] for i in self.database_manager.get_hosts_list()])
        host_description_list = self.network_manager.get_hosts_list(known_hosts_string)
        self.updateHostListTableWidget.emit(host_description_list)
