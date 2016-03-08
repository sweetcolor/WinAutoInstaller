import time
import _thread as thread
from app.winapi_manager.const import ACTIONS


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

    def exec_action(self, action):
        """
        Execute action on the control
        :param action:
        """
        getattr(self.handle_wrapper, action.text())()
        return 0

    def get_actions(self):
        """
        return allowed actions for this object. [(id,action_name),...]
        """
        allowed_actions = []
        obj_actions = dir(self.handle_wrapper.WrapperObject())
        for action in ACTIONS:
            if action in obj_actions:
                allowed_actions.append(action)
        allowed_actions.sort()
        return allowed_actions

    def _highlight_control(self, repeat=1):
        while repeat > 0:
            repeat -= 1
            self.handle_wrapper.DrawOutline('red', thickness=1)
            time.sleep(0.3)
            self.handle_wrapper.DrawOutline(colour=0xffffff, thickness=1)
            time.sleep(0.2)
        return 0
