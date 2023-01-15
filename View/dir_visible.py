from module_view import CModuleBase, CMultiModuleView
from PyQt5.QtWidgets import QPlainTextEdit, QApplication, QWidget
import sys


class CDirVisible(CModuleBase):
    def __init__(self, parent=None):
        super(CDirVisible, self).__init__(parent)
        self._switch_widget.setText('Dir List')
        self._create_widget()

    def _create_widget(self):
        self._widget = QPlainTextEdit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c_wg = CDirVisible()
    multi_module_view = CMultiModuleView()
    multi_module_view.add_widget(c_wg)
    multi_module_view.show()
    sys.exit(app.exec_())
