import os
import json

from PyQt5 import QtCore

from base.record import Record

class Project(QtCore.QObject):
    project_updated = QtCore.pyqtSignal(name="project_updated")
    def __init__(self, project_path: str = None):
        #Project
        self._project_name = ""
        self._project_folder = ""
        self._speaker = ""
        self._language = ""
        self._n_record = 0
        self._audio_length = 0.0
        self._n_words = 0
        self._n_sentence = 0
        self._total_word = 0
        self._metadata_file = ""
        self._record_folder = ""
        self._record_prefix = ""
        
        #Audio
        self._sampling_rate = 16000 #Hz
        self._encoding = 2 #bytes

    def open_project(self, project_path:str):
        with open(project_path, 'r') as f:
            manifest = json.load(f)
        self._project_name = manifest['project_name']
        self._speaker = manifest['speaker']
        self._language = manifest['language']
        self._n_record = manifest['n_record']
        self._n_sentence = manifest.get('n_sentences', 0)
        self._total_word = manifest['total_word']
        self._audio_length = manifest['audio_length'] # s
        self._n_words = manifest['n_words']
        self._record_prefix = manifest['record_prefix']
        self._sampling_rate = manifest['sampling_rate']
        self._encoding = manifest['encoding']


    def create_project(self, project_folder, project_name, speaker, language, record_prefix, sampling_rate: int = 16000, encoding: int = 2):
        self._project_name = project_name
        self._project_folder = os.path.join(project_folder, project_name)
        self._metadata_file = os.path.join(self._project_folder, "metadata.csv")
        self._record_folder = os.path.join(self._project_folder, "audio")
        self._record_prefix = record_prefix
        self._speaker = speaker
        self._language = language
        self._sampling_rate = sampling_rate

        #Create project folder
        os.mkdir(self._project_folder)
        os.mkdir(self._record_folder)
        with open(self._metadata_file, 'w'):
            pass
        
        #write manifest
        self._write_project_file()

    def _write_project_file(self):
        manifest = dict()
        manifest['project_name'] = self._project_name
        manifest['speaker'] = self._speaker
        manifest['n_record'] = self._n_record
        manifest['audio_length'] = self._audio_length
        manifest['n_words'] = self._n_words
        manifest['record_prefix'] = self._record_prefix
        manifest['sampling_rate'] = self._sampling_rate
        manifest['encoding'] = self._encoding
        manifest['language'] = self._language
        manifest['total_word'] = self._total_word
        manifest['n_sentences'] = self._n_sentence
        with open(os.path.join(self._project_folder, self._project_name)+".proj", 'w') as f:
            json.dump(manifest, f)

    def add_text(self, sentences: list):
        if not os.path.isfile(self.project_base_text):
            with open(self.project_base_text, 'w') as f:
                f.writelines(sentences)
        else:
            with open(self.project_base_text, 'w+') as f:
                f.writelines(sentences)
        
        # Update stats
        self._n_sentence += len(sentences)
        w_c = 0
        for sentence in sentences:
            w_c += len(sentence.split(' '))
        self._n_words += w_c
        self._write_project_file()

        self.project_updated.emit()
    
    @property
    def project_base_text(self) -> str:
        return os.path.join(self._project_folder, "text_bank.txt")

    @property
    def project_manifest(self) -> str:
        return os.path.join(self._project_folder, self._project_name+'.proj')

    @property
    def formated_duration(self) -> str:
        hour, minute, second = 0, 0, self._audio_length
        hour = second // 3600
        second -= hour * 3600
        minute = second // 60
        second -= minute * 60
        return "{:3}h {:2}m {:2}s".format(int(hour), int(minute), int(second))
 