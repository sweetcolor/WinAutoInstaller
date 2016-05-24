import os
from widgets.file_dialog import FileDialog


class TabController:
    def __init__(self, **kwargs):
        self.widget = kwargs['widget']
        managers = kwargs['managers']
        self.installer_manager = managers.installer_manager
        self.network_manager = managers.network_manager
        self.database_manager = managers.database_manager
        self.window_manager = managers.window_manager
        self._last_dir = self._default_last_opened_dir()

    def get_installer_path(self):
        dialog = FileDialog()
        dialog.setFileMode(FileDialog.ExistingFiles)
        open_files = dialog.getOpenFileName(self.widget, 'Open installer', self._last_dir,
                                            '*.exe;;*.msi;;All files (*.*)')
        self._last_dir = os.path.dirname(open_files[0])
        return list(filter(bool, open_files))

    def connect_slots(self):
        pass

    @staticmethod
    def _default_last_opened_dir():
        return os.path.join(os.getcwd(), 'test', 'test_installer')
