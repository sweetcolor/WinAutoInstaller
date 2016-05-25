from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
from app.lib.thread_decorator import thread
import time


class WindowManager(QObject):
    updateHostListTableWidget = pyqtSignal(list, name='updateHostListTableWidget')

    def __init__(self, window_controller):
        self.network_manager = window_controller.network_manager
        self.database_manager = window_controller.database_manager
        super().__init__()

    @thread
    def update_host_list(self, full_update=False, range_address=None):
        time.sleep(1)
        curr_hosts = self.database_manager.get_hosts_list()
        if full_update or not curr_hosts:
            host_description_list = self.network_manager.get_hosts_list(range_address)
            self.database_manager.update_hosts_list(host_description_list)
        else:
            known_hosts_string = ' '.join([i[0] for i in curr_hosts])
            host_description_list = self.network_manager.get_hosts_list(known_hosts_string)
        self.updateHostListTableWidget.emit(host_description_list)
