class DialogController:
    def __init__(self, dialog):
        self.dialog = dialog
        self.dialog.exec_()
