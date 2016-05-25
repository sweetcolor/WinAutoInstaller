from app.view_py.input_network_range import Ui_Dialog


class InputNetworkRangeController(Ui_Dialog):
    def __init__(self, dialog):
        self.dialog = dialog
        super(InputNetworkRangeController, self).__init__()
        self.setupUi(self.dialog)
        self.dialog.exec_()

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

