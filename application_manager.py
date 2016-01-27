import pywinauto
from pywinauto import taskbar


class InstallerManager:
    def __init__(self):
        self.app = pywinauto.Application()
        self.installer = None

    def start_installer(self, file_path):
        self.app.start(file_path)
        # installer = self.app.window_()
        installer = self.app.window_(**{'visible_only': False, 'class_name_re': "#32770"})
        print(installer._ctrl_identifiers())

    def get_programs_list(self):
        handles = pywinauto.findwindows.find_windows()
        windows = []
        task_bar_handle = pywinauto.taskbar.TaskBarHandle()
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
