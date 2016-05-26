from app.view_py.input_network_range import Ui_Dialog
from app.controllers.dialog_controller import DialogController


class InputNetworkRangeController(DialogController, Ui_Dialog):
    def __init__(self, dialog):
        self.setupUi(dialog)
        super().__init__(dialog)

    def get_network_range(self):
        net_range = ''
        if self.dialog.result():
            net_range += self.ip1_octetLineEdit.text() + '.'
            net_range += self.ip2_octetLineEdit.text() + '.'
            net_range += self.ip3_octetLineEdit.text() + '.'
            net_range += self.ip4_octetBeginLineEdit.text() + '-'
            net_range += self.ip4_octetEndLineEdit.text()
            return net_range
        return net_range

