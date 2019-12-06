import os
import sys
import json
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

from base.project import Project
from ui.forms.home import Ui_Home
from ui.create_dialog import Create_Dialog

if getattr(sys, 'frozen', False):
    DIR_PATH = os.path.dirname(sys.executable)
else:
    DIR_PATH = os.path.dirname(os.path.dirname(__file__))

class Home(QtWidgets.QWidget):
    project_openned = QtCore.pyqtSignal(Project, name="project_openned")
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        self._last_project_path = None

        linagora_icon = QtGui.QPixmap(os.path.join(DIR_PATH, "ui/icons/linagora-labs.png"))
        self.ui.banner_LB.setPixmap(linagora_icon)

        self._load_user_prefs()
        
        # CONNECT
        self.ui.open_PB.clicked.connect(self._on_open_clicked)
        self.ui.create_PB.clicked.connect(self._on_create_clicked)
        self.ui.open_last_PB.clicked.connect(self._on_open_last)

    def _on_open_clicked(self):
        res = QtWidgets.QFileDialog.getOpenFileName(self, "Select a project file", "", "Project file (*.proj)")[0]
        if len(res) != 0:
            project = Project()
            try:
                project.open_project(res)
            except:
                #TODO handle
                return
            self._update_user_prefs(project)
            self.project_openned.emit(project)

    def _on_open_last(self):
        project = Project()
        try:
            project.open_project(self._last_project_path)
        except:
            #TODO handle
            return
        self.project_openned.emit(project)
        

    def _on_create_clicked(self):
        dialog = Create_Dialog(self)
        dialog.show()
        dialog.project_created.connect(self._on_project_created)

    def _on_project_created(self, project):
        self._update_user_prefs(project)
        self.project_openned.emit(project)
        

    def _load_user_prefs(self):
        pref_path = os.path.join(DIR_PATH, ".user_preferences.json")
        if not os.path.isfile(pref_path):
            man = dict()
            man['last_project'] = {"project_name": "", "project_location":""}
            try:
                with open(pref_path, 'w') as f:
                    json.dump(man, f)
            except Exception as e:
                #TODO: Handle
                return
        with open(pref_path, 'r') as f:
            prefs = json.load(f)['last_project']
        
        if len(prefs['project_name']) > 1:
            self.ui.open_last_PB.setText("Open Last project : {}".format(prefs['project_name']))
            self.ui.open_last_PB.setToolTip(prefs['project_location'])
            self._last_project_path = prefs['project_location']
        else:
            self.ui.open_last_PB.hide()
            self.ui.last_project_label.hide()

    def _update_user_prefs(self, project: Project):
        pref_path = os.path.join(DIR_PATH, ".user_preferences.json")
        man = dict()
        man['last_project'] = {"project_name": project._project_name, "project_location":project.project_manifest}

        with open(pref_path, 'w') as f:
            json.dump(man, f)
