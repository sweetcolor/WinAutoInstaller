import sys
from PyQt5 import QtWidgets
from app.main_window import MainWindow


def run(argv):
    app = QtWidgets.QApplication(argv)
    app.setStyle('fusion')
    window = QtWidgets.QMainWindow()
    main_window = MainWindow(window)
    window.show()
    sys.exit(app.exec_())
