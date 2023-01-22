from module_view import CModuleBase, CMultiModuleView
from PyQt5 import QtWidgets
import sys
import os


class CDirVisible(CModuleBase):
    BLANKS_NUM = 6

    def __init__(self, parent=None):
        self.dir_edit = None
        self.info_plain = None
        self.list_info = ''
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
        root = self.dir_edit.text()
        self.list_dir(root)
        self.info_plain.setPlainText(self.list_info)

    def list_dir(self, root, level=0):
        for path, dirs, files in os.walk(root):
            if level == 0:
                self.list_info = (' ' * self.BLANKS_NUM * level + path + '\n')
                # print('    ' * level + path)
            for file in files:
                self.list_info += (' ' * self.BLANKS_NUM * level + '  |___' + file + '\n')
                # print('    ' * level + '  |___' + file)
            for sub_dir in dirs:
                self.list_info += (' ' * self.BLANKS_NUM * level + '  |___' + sub_dir + '\n')
                # print('    ' * level + '  |___' + sub_dir)
                if sub_dir[0] != '.':
                    self.list_dir(os.path.join(path, sub_dir), level + 1)
            break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    multi_module_view = CMultiModuleView()
    multi_module_view.add_widget(CDirVisible())
    multi_module_view.show()
    sys.exit(app.exec_())
