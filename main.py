import sys

from PyQt5 import QtWidgets

from app.managers.window_manager import Window


class MainWindow(Window):
    def __init__(self, form):
        self.setupUi(form)
        super().__init__()
        self.connect_slots()

    def connect_slots(self):
        self.openInstallerButton.clicked.connect(self.open_installer)
        self.refreshListButton.clicked.connect(self.refresh_program_list)
        self.updateHostListButton.clicked.connect(self.update_host_list)
        self.fullUpdateHostListButton.clicked.connect(self.full_update_host_list)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())


__author__ = 'Администратор'
