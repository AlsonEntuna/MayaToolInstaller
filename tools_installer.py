import sys
import os
import fnmatch
from tkinter import filedialog
from imp import reload

from PySide6 import QtWidgets
from ui.ToolsInstallerWindow import Ui_Form

import constants as const
reload(const)


class ToolsIntallerWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(ToolsIntallerWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # UI Bindings
        self.ui.btn_browse.clicked.connect(self._browse_tool_module)
        self.ui.btn_install.clicked.connect(self._intsall_tool)

        # Inits
        self._detect_maya_version()

    def _intsall_tool(self):
        module_args = self.ui.txt_module_call.toPlainText()
        # TODO: generate macro script that will be executed in maya

    def _browse_tool_module(self):
        tool_path = filedialog.askdirectory(title='Select tools folder path')
        self.ui.txt_tool_loc.setText(tool_path)

    def _detect_maya_version(self):
        maya_prefs_path = const.get_maya_prefs_path()
        print(maya_prefs_path)
        maya_vers = fnmatch.filter(os.listdir(maya_prefs_path), '20*')
        self.ui.combo_version.addItems(maya_vers)



def main():
    app = QtWidgets.QApplication(sys.argv)

    window = ToolsIntallerWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()    