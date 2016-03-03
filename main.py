import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from app.managers.window_manager import Window


# TODO create single class file
class MainWindow(Window):
    def __init__(self, form):
        self.setupUi(form)
        super().__init__(form)
        self.connect_slots()

    def connect_slots(self):
        self.openInstallerButton.clicked.connect(self.open_installer)
        self.refreshListButton.clicked.connect(self.refresh_program_list)
        self.updateHostListButton.clicked.connect(self.update_host_list)
        self.fullUpdateHostListButton.clicked.connect(self.full_update_host_list)
        self.installerComponentTreeWidget.doubleClicked.connect(self.clicked_on_program_component)
        self.installerComponentTreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.installerComponentTreeWidget.customContextMenuRequested.connect(self.context_menu_of_program_component)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())


__author__ = 'Администратор'
