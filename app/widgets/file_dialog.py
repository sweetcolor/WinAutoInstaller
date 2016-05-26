from PyQt5.QtWidgets import QFileDialog, QTreeView, QPushButton
import os


class FileDialog(QFileDialog):
    def __init__(self, **kwargs):
        self.widget = kwargs['widget']
        QFileDialog.__init__(self, self.widget)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.ExistingFiles)
        buttons = self.findChildren(QPushButton)
        self.openBtn = [x for x in buttons if 'open' in str(x.text()).lower()][0]
        self.openBtn.clicked.disconnect()
        self.openBtn.clicked.connect(self.open_clicked)
        self.tree = self.findChild(QTreeView)
        self.selected_files = ''
        self._last_dir = self._default_last_opened_dir()

    def get_installer_path(self):
        open_files = self.getOpenFileName(self.widget, 'Open installer', self._last_dir,
                                          '*.exe;;*.msi;;All files (*.*)')
        self._last_dir = os.path.dirname(open_files[0])
        return list(filter(bool, open_files))

    # TODO multi select installer1
    def open_clicked(self):
        indexes = self.tree.selectionModel().selectedIndexes()
        files = []
        for i in indexes:
            if i.column() == 0:
                files.append(os.path.join(str(self.directory().absolutePath()), str(i.data().toString())))
        self.selected_files = files
        self.hide()

    def filesSelected(self):
        return self.selected_files

    @staticmethod
    def _default_last_opened_dir():
        return os.path.join(os.getcwd(), 'test', 'test_installer')
