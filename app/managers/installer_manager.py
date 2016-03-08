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
        components_text = self._get_program_components_helper(components)
        return components_text, components

    def _get_program_components_helper(self, components):
        components_text = dict()
        for component in components.keys():
            components_text[component] = self._get_program_components_helper(components[component]['child'])
        return components_text

    def get_programs_list(self):
        return self.process.all_components() if self.process else []
