from PyQt5.QtWidgets import QWidget
from app.view_py.results_installation import Ui_Form


class ResultInstallationController(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
