from PyQt5.QtWidgets import QMenu


class MenuManager(QMenu):
    def __init__(self, installer_component, *__args):
        super().__init__(*__args)
        self.installer_component = installer_component
        self.triggered.connect(self.triggered_action)

    def triggered_action(self, action):
        self.installer_component.exec_action(action)
