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
        windows = dict()
        for w_handle in handles:
            window_ = WinApiWindow(WindowSpecification(dict(handle=w_handle)))
            windows[window_] = list()
            for sub_hwnd in window_.Children():
                windows[window_].append(WinApiWindow(sub_hwnd))
        return windows
