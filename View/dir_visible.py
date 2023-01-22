from module_view import CModuleBase, CMultiModuleView
from PyQt5 import QtWidgets
import sys


class CDirVisible(CModuleBase):
    def __init__(self, parent=None):
        self.dir_edit = None
        self.info_plain = None
        super(CDirVisible, self).__init__(parent)

    def create_widget(self):
        wg = QtWidgets.QWidget()
        v_lay = QtWidgets.QVBoxLayout(wg)
        h_lay = QtWidgets.QHBoxLayout()
        self.dir_edit = QtWidgets.QLineEdit()
        dir_load = QtWidgets.QPushButton('Load Dir')
        dir_show = QtWidgets.QPushButton('Show Dir')
        h_lay.addWidget(self.dir_edit)
        h_lay.addWidget(dir_load)
        h_lay.addWidget(dir_show)
        self.info_plain = QtWidgets.QPlainTextEdit()
        v_lay.addLayout(h_lay)
        v_lay.addWidget(self.info_plain)

        self.dir_edit.setReadOnly(True)
        # dir_load.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Maximum)
        self.info_plain.setReadOnly(True)
        dir_load.clicked.connect(self.load_dir)
        dir_show.clicked.connect(self.show_dir)
        return wg

    def module_name(self):
        return 'Dir Info'

    def load_dir(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a dir')
        self.dir_edit.setText(path)
        pass

    def show_dir(self):
        print('show dir')
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    multi_module_view = CMultiModuleView()
    multi_module_view.add_widget(CDirVisible())
    multi_module_view.show()
    sys.exit(app.exec_())
