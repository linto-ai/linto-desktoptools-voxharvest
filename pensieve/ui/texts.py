from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

from base.project import Project
from ui.forms.texts import Ui_Form
from utils.text import get_cleaner_fun, split_text

class Text_Widget(QtWidgets.QWidget):
    def __init__(self, project: Project):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._project = project

        #CONNECT
        self.ui.add_raw_PB.clicked.connect(self._on_add_raw_clicked)
        self.ui.add_formated_PB.clicked.connect(self._on_add_formated_clicked)

    def _load_text_stats(self):
        pass

    def _on_add_raw_clicked(self):
        res = QtWidgets.QFileDialog.getOpenFileName(self, "Select a text file", "", "All File (*.*)")[0]
        if len(res) > 0:
            clean_fun = get_cleaner_fun(self._project._language)
            with open(res, 'r') as f:
                text = f.read()
            clean_text = clean_fun(text)
            sentences = split_text(clean_text)
            self._project.add_text(sentences)

    def _on_add_formated_clicked(self):
        res = QtWidgets.QFileDialog.getOpenFileName(self, "Select a text file", "", "All File")[0]
        if len(res) > 0:
            pass

        
    
