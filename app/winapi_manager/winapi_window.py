from app.winapi_manager.winapi_object import WinApiObject


class WinApiWindow(WinApiObject):
    def __init__(self, handle_wrapper):
        super().__init__(handle_wrapper)
