from PyQt5 import QtWidgets, QtCore
from abc import ABC, abstractmethod


class CModuleBase(QtCore.QObject):
    signal_activated = QtCore.pyqtSignal(QtWidgets.QWidget)

    def __init__(self, parent=None):
        super(CModuleBase, self).__init__(parent)
        self._name_btn = QtWidgets.QPushButton()
        self._name_btn.clicked.connect(lambda: self.signal_activated.emit(self._widget))
        self._name_btn.setText(self.module_name())
        self._widget = self.create_widget()

    def name_btn(self):
        return self._name_btn

    def main_widget(self):
        return self._widget

    # @abstractmethod
    def create_widget(self):
        pass

    def module_name(self):
        return ''
    

class CMultiModuleView(QtWidgets.QWidget):
    widget_size = QtCore.QSize(1350, 900)

    def __init__(self, parent=None):
        super(CMultiModuleView, self).__init__(parent)
        self._switch_widget = QtWidgets.QWidget()
        self._switch_layout = QtWidgets.QVBoxLayout(self._switch_widget)
        self._switch_layout.addStretch()
        self._stacked_widget = QtWidgets.QStackedWidget()
        self._create_layout()
        self.resize(self.widget_size)

    def _create_layout(self):
        h_lay = QtWidgets.QHBoxLayout(self)
        h_lay.addWidget(self._switch_widget)
        h_lay.addWidget(self._stacked_widget)

    def add_widget(self, module):
        index = self._switch_layout.count()
        self._switch_layout.insertWidget(index - 1, module.name_btn())
        self._stacked_widget.addWidget(module.main_widget())
        module.signal_activated.connect(self._stacked_widget.setCurrentWidget)
