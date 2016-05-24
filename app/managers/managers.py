from app.managers.window_manager import WindowManager
from app.managers.database_manager import DatabaseManager
from app.managers.installer_script_manager import InstallerScriptManager
from app.managers.network_manager import NetworkManager


class Managers:
    def __init__(self):
        self.installer_manager = InstallerScriptManager()
        self.network_manager = NetworkManager()
        self.database_manager = DatabaseManager('winautoinstaller')
        self.window_manager = WindowManager(self)
