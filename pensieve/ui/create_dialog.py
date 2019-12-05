import os

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

from utils.text import SUPPORTED_LANG
from base.project import Project
from ui.forms.create_dialog import Ui_Dialog

class Create_Dialog(QtWidgets.QDialog):
    project_created = QtCore.pyqtSignal(Project, name="project_created")
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._project = Project()
        self._init_language_CB()

        #CONNECT
        self.ui.create_PB.clicked.connect(self._on_create_clicked)
        self.ui.cancel_PB.clicked.connect(self.close)
        self.ui.browse_PB.clicked.connect(self._on_browse_clicked)
        self.ui.project_name_LE.textChanged.connect(self._on_project_name_changed)

    def _on_create_clicked(self):
        if not self._check_inputs():
            return
        self._project.create_project(self.ui.browse_LE.text(),
                                     self.ui.project_name_LE.text(),
                                     self.ui.speaker_LE.text(),
                                     self.selected_language,
                                     self.ui.prefix_LE.text(),
                                     self.ui.sample_rate_CoB.currentText(),
                                     self.ui.encoding_CoB.currentText())
        self.project_created.emit(self._project)
        self.close()

    def _init_language_CB(self):
        for supp_lang in SUPPORTED_LANG:
            self.ui.language_CB.addItem(supp_lang)

    def _on_project_name_changed(self, value: str):
        self.ui.prefix_LE.setText(value.strip().replace(' ', '_').lower())

    def _on_browse_clicked(self):
        res = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a parent directory", "/home/")
        if len(res) != 0:
            self.ui.browse_LE.setText(res)
            self.ui.browse_LE.setToolTip(res)

    def _check_inputs(self) -> bool:
        for input in [self.ui.project_name_LE, self.ui.speaker_LE, self.ui.prefix_LE]:
            if len(input.text()) == 0:
                #TODO: warning message
                input.setFocus()
                return False

        if not os.path.isdir(self.ui.browse_LE.text()):
            self.ui.browse_PB.setFocus()
            #TODO warning message
            return False
        
        return True
    
    @property
    def selected_language(self) -> str:
        return self.ui.language_CB.currentText()