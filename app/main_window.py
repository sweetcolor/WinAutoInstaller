from PyQt5.QtCore import Qt
from app.managers.window_manager import Window


class MainWindow(Window):
    def __init__(self, form):
        self.setupUi(form)
        super().__init__(form)
        self.connect_slots()

    def connect_slots(self):
        # createScriptTab
        self.openInstallerButton.clicked.connect(self.run_installer)
        self.refreshListButton.clicked.connect(self.refresh_program_list)
        self.installerComponentTreeWidget.doubleClicked.connect(self.clicked_on_program_component)
        self.installerComponentTreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.installerComponentTreeWidget.customContextMenuRequested.connect(self.context_menu_of_program_component)

        # hostManagerTab
        # hostListVerticalLayout
        self.fullUpdateHostListButton.clicked.connect(self.full_update_host_list)
        self.updateHostListButton.clicked.connect(self.update_host_list)
        self.startInstalationOnHostsButton.clicked.connect(self.start_installation_on_host)
        # scriptsListVerticalLayout
        self.updateScriptsListPushButton.clicked.connect(self.update_scripts_list)

        # installerManagerTab
        self.addInstallerPushButton.clicked.connect(self.add_installer)
        self.deleteInstallerPushButton.clicked.connect(self.delete_installer)
        self.saveChangesPushButton.clicked.connect(self.save_changes_in_database)
        self.updateInstallerListPushButton.clicked.connect(self.update_installer_list)
