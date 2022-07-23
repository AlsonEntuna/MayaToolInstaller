import sys

from PySide6 import QtWidgets
from ui.ToolsInstallerWindow import Ui_Form

class ToolsIntallerWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(ToolsIntallerWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # UI Bindings

    def _intsall_tool(self):
        pass

    def _browse_tool_module(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = ToolsIntallerWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()    