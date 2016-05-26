from PyQt5.QtCore import Qt

from app.controllers.tab_controller import TabController
from app.managers.menu_manager import MenuManager
from app.view_py.create_script import Ui_Form
from app.widgets.installerTreeWidgetItem import InstallerTreeWidgetItem


class CreateScriptTabController(TabController, Ui_Form):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self.widget)
        self.installer_wind_components_list = list()
        self.components = dict()
        self.installer_winds_list = list()
        self.connect_slots()

    def run_installer(self):
        installer_path = self.get_installer_path()
        installer_path = installer_path[0] if installer_path else None
        if installer_path:
            self.installer_manager.start_installer(installer_path)
            self.refresh_program_list()

    def refresh_program_list(self):
        self.installer_wind_components_list.clear()
        self.installerComponentTreeWidget.clear()
        components_text, components = self.installer_manager.get_program_components()
        self._refresh_program_list_helper(self.installerComponentTreeWidget, components)

    def _refresh_program_list_helper(self, parent, components):
        for text in components.keys():
            wind_item = InstallerTreeWidgetItem(components[text]['component'], parent)
            wind_item.setText(0, text)
            if components[text]['child']:
                self._refresh_program_list_helper(wind_item, components[text]['child'])

    def clicked_on_program_component(self, index):
        inst_tree_widget_item = self.installerComponentTreeWidget.itemFromIndex(index)
        inst_tree_widget_item.get_installer_component().highlight_control()

    def context_menu_of_program_component(self, event):
        clicked_item_model_index = self.installerComponentTreeWidget.indexAt(event)
        clicked_item_index = self.installerComponentTreeWidget.itemFromIndex(clicked_item_model_index)
        item = clicked_item_index.get_installer_component()
        context_menu = MenuManager(item, self.widget)
        for action in item.get_actions():
            context_menu.addAction(action)
        context_menu.exec(self.widget.mapToGlobal(event))
        self.refresh_program_list()

    def connect_slots(self):
        self.openInstallerButton.clicked.connect(self.run_installer)
        self.refreshListButton.clicked.connect(self.refresh_program_list)
        self.installerComponentTreeWidget.doubleClicked.connect(self.clicked_on_program_component)
        self.installerComponentTreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.installerComponentTreeWidget.customContextMenuRequested.connect(self.context_menu_of_program_component)
