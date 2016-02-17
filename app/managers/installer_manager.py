import pywinauto
from app.winapi_manager.winapi_process import WinApiProcess


# TODO rename all manager -> interface
# TODO create controllers
class InstallerManager:
    def __init__(self):
        self.app = pywinauto.Application()
        self.installer = None
        self.process = None

    def start_installer(self, file_path):
        self.app.start(file_path)
        self.process = WinApiProcess(self.app.process)

    def get_program_components(self):
        components = self.process.all_components() if self.process else []
        components_text = dict()
        components_for_tree_widget = dict()
        for wind in components.keys():
            components_text[wind.get_text()] = [child.get_text() for child in components[wind]]
            components_for_tree_widget[wind.get_text()] = wind
            for child in components[wind]:
                components_for_tree_widget[child.get_text()] = child
        return components_text, components_for_tree_widget

    def get_programs_list(self):
        return self.process.all_components() if self.process else []
