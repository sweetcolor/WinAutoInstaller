import pywinauto
from pywinauto import taskbar
from pywinauto import controls


class InstallerManager:
    def __init__(self):
        self.app = pywinauto.Application()
        self.installer = None
        self.process_id = None

    def start_installer(self, file_path):
        self.app.start(file_path)
        self.process_id = self.app.process

    def get_program_components(self, handles=None):
        handles = pywinauto.findwindows.find_windows(process=self.process_id) if not handles else handles
        windows = dict()
        for w_handle in handles:
            self.app = pywinauto.Application()
            wind = self.app.window_(handle=w_handle)
            window_texts = wind.Texts()
            window_texts = filter(bool, window_texts)  # filter out '' and None items
            if not window_texts:
                window_texts = 'Window#%s' % w_handle
            else:
                # title = ', '.join(texts).encode(encoding='utf-8').decode('cp1251')
                window_texts = ', '.join(window_texts)
            windows[window_texts] = []
            hwnd = controls.WrapHandle(w_handle)
            for sub_hwnd in hwnd.Children():
                children_texts = sub_hwnd.Texts()
                if children_texts:
                    children_texts = list(filter(bool, children_texts))  # filter out '' and None items

                if children_texts:  # check again after the filtering
                    children_texts = ', '.join(children_texts)
                else:
                    continue
                windows[window_texts].append(children_texts)
        return windows

    def get_programs_list(self):
        handles = pywinauto.findwindows.find_windows()
        windows = []
        task_bar_handle = taskbar.TaskBarHandle()
        for w_handle in handles:
            wind = self.app.window_(handle=w_handle)
            if w_handle == task_bar_handle:
                title = 'TaskBar'
            else:
                texts = wind.Texts()
                texts = filter(bool, texts)  # filter out '' and None items
                if not texts:
                    title = 'Window#%s' % w_handle
                else:
                    # title = ', '.join(texts).encode(encoding='utf-8').decode('cp1251')
                    title = ', '.join(texts)
            windows.append(title)
        windows.sort(key=lambda name: name.lower())
        return windows
