import sys
from PyQt5.QtWidgets import QApplication
from app.controllers.window_controller import WindowController


def run(argv):
    app = QApplication(argv)
    app.setStyle('fusion')
    window = WindowController()
    window.show()
    sys.exit(app.exec_())
