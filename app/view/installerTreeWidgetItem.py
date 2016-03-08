from PyQt5.QtWidgets import QTreeWidgetItem


class InstallerTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, installer_component, *__args):
        super().__init__(*__args)
        self.installer_component = installer_component

    def get_installer_component(self):
        return self.installer_component
