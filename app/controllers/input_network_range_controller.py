from app.view_py.input_network_range import Ui_Dialog


class InputNetworkRange(Ui_Dialog):
    def __init__(self, dialog):
        super(InputNetworkRange, self).__init__()
        self.setupUi(dialog)
        dialog.exec_()
