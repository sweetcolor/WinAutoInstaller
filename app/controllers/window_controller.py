from app.managers.managers import Managers
from app.controllers.create_script_tab_controller import CreateScriptTabController
from app.controllers.host_manager_tab_controller import HostManagerTabController
from app.controllers.installer_manager_tab_controller import InstallerManagerTabController
from app.view_py.mainwindow import Ui_MainWindow


class WindowController(Ui_MainWindow):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)
        kwargs = {
            'widget': self.createScriptTab,
            'managers': Managers()
        }
        self.create_script_tab_controller = CreateScriptTabController(**kwargs)
        kwargs['widget'] = self.hostManagerTab
        self.host_manager_tab_controller = HostManagerTabController(**kwargs)
        kwargs['widget'] = self.installerManagerTab
        self.installer_manager_tab_controller = InstallerManagerTabController(**kwargs)

__author__ = 'Администратор'
