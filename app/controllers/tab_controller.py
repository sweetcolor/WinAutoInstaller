from app.widgets.file_dialog import FileDialog


class TabController(FileDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        managers = kwargs['managers']
        self.installer_manager = managers.installer_manager
        self.network_manager = managers.network_manager
        self.database_manager = managers.database_manager
        self.window_manager = managers.window_manager

    def connect_slots(self):
        pass
