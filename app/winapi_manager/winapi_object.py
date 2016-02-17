import time
import _thread as thread


class WinApiObject:
    def __init__(self, handle_wrapper):
        self.handle_wrapper = handle_wrapper

    def __getattr__(self, item):
        return getattr(self.handle_wrapper, item)

    def get_text(self):
        window_texts = self.handle_wrapper.Texts()
        window_texts = list(filter(bool, window_texts))
        if not window_texts:
            return str(self)
        return ', '.join(window_texts)

    def highlight_control(self):
        # TODO if self._check_visibility():
        thread.start_new_thread(self._highlight_control, (3,))
        return 0

    def _highlight_control(self, repeat=1):
        while repeat > 0:
            repeat -= 1
            self.handle_wrapper.DrawOutline('red', thickness=1)
            time.sleep(0.3)
            self.handle_wrapper.DrawOutline(colour=0xffffff, thickness=1)
            time.sleep(0.2)
        return 0
