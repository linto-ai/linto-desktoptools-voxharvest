import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

from base.project import Project
from utils.audio import Recorder
from ui.forms.recording import Ui_recording_widget

class Record_Widget(QtWidgets.QWidget):
    def __init__(self, project: Project):
        super().__init__()
        self.ui = Ui_recording_widget()
        self.ui.setupUi(self)

        self.project = project
        self.project.project_updated.connect(self._load_sentences)

        self._load_sentences()
         
        self.recorder = Recorder(self.project)
        self._recording = False

        #Shortcuts
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Space), self)
        shortcut.activated.connect(self._on_shortcut_record)

        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_L), self)
        shortcut.activated.connect(self._on_listen_clicked)

        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self)
        shortcut.activated.connect(self._on_validate_clicked)
        

        #CONNECT
        self.ui.skip_PB.clicked.connect(self._on_skip_clicked)
        self.ui.record_PB.clicked.connect(self._on_record_clicked)
        self.ui.stop_PB.clicked.connect(self._on_stop_clicked)
        self.ui.listen_PB.clicked.connect(self._on_listen_clicked)
        self.ui.validate_PB.clicked.connect(self._on_validate_clicked)
        self.ui.split_PB.clicked.connect(self._on_split_clicked)
        self.ui.remove_PB.clicked.connect(self._on_remove_clicked)
    
    def _load_sentences(self):
        try:
            with open(self.project.project_base_text, 'r') as f:
                sentences = f.readlines()
                self.sentences = list(zip(range(len(sentences)), sentences))
        except:
            self.setEnabled(False)
        else:
            self.setEnabled(True)
            self._next_sentence()
        
        
    def _next_sentence(self):
        self.index, self.current_sentence = self.sentences.pop(0)
        self.ui.sentence_TE.setText(self.current_sentence)
        self.ui.sentence_index_SP.setValue(self.index)

        self.ui.record_PB.setEnabled(True)
        self.ui.stop_PB.setEnabled(False)
        self.ui.listen_PB.setEnabled(False)
        self.ui.validate_PB.setEnabled(False)

    def _on_skip_clicked(self):
        self.sentences.append((self.index, self.current_sentence))
        self._next_sentence()

    def _on_split_clicked(self):
        pos = self.ui.sentence_TE.textCursor().position()
        if pos <= 1:
            return
        to_keep = self.ui.sentence_TE.toPlainText()[:pos]
        to_next = self.ui.sentence_TE.toPlainText()[pos:]
        self.ui.sentence_TE.setText(to_keep)
        self.sentences.insert(0, [self.index, to_next])

    def _on_remove_clicked(self):
        self._next_sentence()

    def _on_shortcut_record(self):
        if self._recording:
            self._on_stop_clicked()
        else:
            self._on_record_clicked()

    def _on_record_clicked(self):
        self.ui.record_PB.setEnabled(False)
        self.ui.stop_PB.setEnabled(True)
        self.ui.listen_PB.setEnabled(False)
        self.ui.validate_PB.setEnabled(False)

        self.recorder.start_recording()
        self._recording = True

    def _on_stop_clicked(self):
        self.ui.record_PB.setEnabled(True)
        self.ui.stop_PB.setEnabled(False)
        self.ui.listen_PB.setEnabled(True)
        self.ui.validate_PB.setEnabled(True)

        self.recorder.stop_recording()
        self._recording = False

    def _on_listen_clicked(self):
        if len(self.recorder.buffer) == 0:
            return
        self.recorder.play_audio()

    def _on_validate_clicked(self):
        if len(self.recorder.buffer) == 0:
            return
        self.project.add_sample(self.recorder,self.current_sentence, self.ui.sentence_TE.toPlainText())
        self.recorder.clear_buffer()
        self._update_text_bank()
        self._next_sentence()

    def _update_text_bank(self):
        with open(self.project.project_base_text, 'w') as f:
            f.write("".join([s[1] for s in self.sentences]))
        self._load_sentences()