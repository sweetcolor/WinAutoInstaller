from form import Ui_MainWindow
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog
from application_manager import InstallerManager
import os


class Window(Ui_MainWindow):
    def __init__(self, widget=None):
        super(Window, self).__init__()
        # self.widget = widget
        self._last_dir = self._default_last_opened_dir()
        self.tree_widgets_list = []
        self.installer_manager = InstallerManager()
        self.refresh_program_list()

    def refresh_program_list(self):
        self.tree_widgets_list.clear()
        self.treeWidget.clear()
        windows = self.installer_manager.get_programs_list()
        for i in windows:
            self.tree_widgets_list.append(QTreeWidgetItem(self.treeWidget))
            self.tree_widgets_list[-1].setText(0, i)

    def open_installer(self):
        installer_path = QFileDialog().getOpenFileName(self.widget, 'Open installer', self._last_dir, '*.exe *.msi')
        self.installer_manager.start_installer(installer_path[0])

    def _last_opened_dir(self):
        if self._last_dir is None:
            self._last_dir = self._default_last_opened_dir()

    @staticmethod
    def _default_last_opened_dir():
        # return os.environ['USERPROFILE']
        return os.getcwd()



__author__ = 'Администратор'
