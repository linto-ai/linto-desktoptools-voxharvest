from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

from base.project import Project
from ui.forms.resume import Ui_Form

class Resume_Widget(QtWidgets.QWidget):
    project_closed = QtCore.pyqtSignal(name="project_closed")
    switch_to_text = QtCore.pyqtSignal(name="switch_to_text")
    switch_to_record = QtCore.pyqtSignal(name="switch_to_record")
    def __init__(self, project: Project):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._project = project
        self._project.project_updated.connect(self._update_values)
        self._update_values()
        
        #CONNECT
        self.ui.close_PB.clicked.connect(self._on_close_clicked)
        self.ui.add_text_PB.clicked.connect(self.switch_to_text.emit)
        self.ui.record_PB.clicked.connect(self.switch_to_record.emit)
        

    def _update_values(self):
        #Project
        self.ui.project_name_LE.setText(self._project._project_name)
        self.ui.speaker_LE.setText(self._project._speaker)
        self.ui.language_LE.setText(self._project._language)

        #Texts
        self.ui.sentences_read_SP.setValue(self._project._n_record)
        self.ui.sentences_total_SP_2.setValue(self._project._n_sentence)
        self.ui.percent_label.setText("({:0>2.2%})".format(self._project._n_record / max(self._project._n_sentence, 1)))

        self.ui.words_read_SP.setValue(self._project._n_words)
        self.ui.words_total_SP.setValue(self._project._total_word)
        self.ui.percent_word_label.setText("({:0>2.2%})".format(self._project._n_words / max(self._project._total_word, 1)))
        
        #Audio
        self.ui.n_samples_SP.setValue(self._project._n_record)
        self.ui.total_duration_LE.setText(self._project.formated_duration)

    def _on_close_clicked(self):
        #TODO prompt
        self.project_closed.emit()