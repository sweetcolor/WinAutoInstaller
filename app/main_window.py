from PyQt5.QtCore import Qt

from app.controllers.window_controller import WindowController


class MainWindowController(WindowController):
    def __init__(self, form):
        self.setupUi(form)
        super().__init__(form)
        self.connect_slots()


        # hostManagerTab
        # hostListVerticalLayout

        # installerManagerTab
