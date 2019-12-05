import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from base.project import Project
from ui.forms.mainwindow import Ui_MainWindow
from ui.record_widget import Record_Widget
from ui.resume import Resume_Widget
from ui.home import Home
from ui.texts import Text_Widget

if getattr(sys, 'frozen', False):
    DIR_PATH = os.path.dirname(sys.executable)
else:
    DIR_PATH = os.path.dirname(os.path.dirname(__file__))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.project = None

        self._layout = QtWidgets.QVBoxLayout()
        self.ui.central_widget.setLayout(self._layout)

        self._load_icons()
        self._set_button_visible(False)

        self._home_panel = None
        self._resume_panel = None
        self._record_panel = None
        self._texts_panel = None
        self._audio_panel = None
        
        #CONNECT
        self.ui.home_PB.clicked.connect(self._open_resume_panel)
        self.ui.text_PB.clicked.connect(self._open_texts_panel)

    def _open_record_panel(self):
        if self._record_panel is None:
            self._record_panel = Record_Widget(self.project)

        self._layout.addWidget(self._record_panel)

    def _open_resume_panel(self):
        if self._resume_panel is None:
            self._resume_panel = Resume_Widget(self.project)
            self._resume_panel.project_closed.connect(self._on_project_close)
            self._layout.addWidget(self._resume_panel)
        self.switch_panel(self._resume_panel)

    def _open_home_panel(self):
        if self._home_panel is None:
            self._home_panel = Home()
            self._layout.addWidget(self._home_panel)
            self._home_panel.project_openned.connect(self._on_project_opened)
        self.switch_panel(self._home_panel)

    def _open_texts_panel(self):
        if self._texts_panel is None:
            self._texts_panel = Text_Widget(self.project)
            self._layout.addWidget(self._texts_panel)
        self.switch_panel(self._texts_panel)

    def _load_icons(self):
        for button, icon_path in zip([self.ui.home_PB, self.ui.text_PB, self.ui.record_PB, self.ui.setting_PB],
                                     ["home_icon.png", "text_icon.png", "record_icon.png", "setting_icon.png"]):
            icon = QtGui.QPixmap(os.path.join(DIR_PATH, "ui/icons/", icon_path))

            button.setIcon(QtGui.QIcon(icon))
            button.setIconSize(QtCore.QSize(90,90))
    
    def _set_button_visible(self, visible):
        for button in [self.ui.home_PB, self.ui.text_PB, self.ui.record_PB, self.ui.setting_PB]:
            button.setVisible(visible)

    def _on_project_opened(self, project):
        self.project = project
        self._open_resume_panel()
        self.switch_panel(self._resume_panel)
        self._set_button_visible(True)

    def _on_project_close(self):
        self.switch_panel(self._home_panel)
        self._resume_panel = None
        self._record_panel = None 
        self._texts_panel = None 
        self._audio_panel = None
            

    def _empty_layout(self):
        pass

    def switch_panel(self, panel_to_display):
        for panel in [self._home_panel, self._resume_panel, self._record_panel, self._texts_panel, self._audio_panel]:
            if panel is not None and panel is not panel_to_display:
                panel.hide()
            panel_to_display.show()
            

    
