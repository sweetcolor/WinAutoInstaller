import sys
from PyQt5 import QtWidgets
from app.controllers.window_controller import WindowController


def run(argv):
    app = QtWidgets.QApplication(argv)
    app.setStyle('fusion')
    window = QtWidgets.QMainWindow()
    window_controller = WindowController(window)
    window.show()
    sys.exit(app.exec_())
