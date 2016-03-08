from pywinauto import findwindows
from pywinauto import Application
from app.winapi_manager.winapi_window import WinApiWindow
from pywinauto import WindowSpecification


class WinApiProcess:
    def __init__(self, process_id=None):
        self.app = Application()
        self.process_id = process_id

    def all_components(self):
        handles = findwindows.find_windows(process=self.process_id)
        return self._components_helper(handles)

    def _components_helper(self, child_handles):
        windows = dict()
        for c_handle in child_handles:
            window_ = WinApiWindow(WindowSpecification(dict(handle=c_handle)))
            windows[window_.get_text()] = dict()
            windows[window_.get_text()]['component'] = window_
            windows[window_.get_text()]['child'] = self._components_helper(window_.Children())
        return windows
