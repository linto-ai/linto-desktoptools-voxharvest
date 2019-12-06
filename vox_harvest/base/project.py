import os
import json

from PyQt5 import QtCore

class Project(QtCore.QObject):
    project_updated = QtCore.pyqtSignal(name="project_updated")
    def __init__(self, project_path: str = None):
        #Project
        super().__init__()
        
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

        self._words_stats = dict()
        #Audio
        self._sampling_rate = 16000 #Hz
        self._encoding = 2 #bytes

    def open_project(self, project_path:str):
        with open(project_path, 'r') as f:
            manifest = json.load(f)
        self._project_folder = os.path.dirname(project_path)
        self._project_name = manifest['project_name']
        self._speaker = manifest['speaker']
        self._language = manifest['language']
        self._audio_length = manifest['audio_length'] # s
        self._record_prefix = manifest['record_prefix']
        self._sampling_rate = manifest['sampling_rate']
        self._encoding = manifest['encoding']

        self._restat()

    def create_project(self, project_folder, project_name, speaker, language, record_prefix, sampling_rate: int = 16000, encoding: int = 2):
        self._project_name = project_name
        self._project_folder = os.path.join(project_folder, project_name)
        self._record_prefix = record_prefix
        self._speaker = speaker
        self._language = language
        self._sampling_rate = sampling_rate

        #Create project folder
        os.mkdir(self._project_folder)
        os.mkdir(self._record_folder)
        with open(self.metadata_path, 'w'):
            pass
        
        #write manifest
        self._write_project_file()

    def _write_project_file(self):
        manifest = dict()
        manifest['project_name'] = self._project_name
        manifest['speaker'] = self._speaker
        manifest['audio_length'] = self._audio_length
        manifest['record_prefix'] = self._record_prefix
        manifest['sampling_rate'] = self._sampling_rate
        manifest['encoding'] = self._encoding
        manifest['language'] = self._language
        with open(self.project_manifest, 'w') as f:
            json.dump(manifest, f)

    def add_text(self, sentences: list):
        mode = 'a+' if os.path.isfile(self.project_base_text) else 'w+'

        f = open(self.project_base_text, mode)
        w_c = 0
        for sentence in sentences:
            w_c += len(sentence.split(' '))
            f.write(sentence + "\n")
        
        # Update stats
        self._n_sentence += len(sentences)            
        self._total_word += w_c

        self._restat()
        self.project_updated.emit()

    def add_sample(self,recorder, raw_text, corrected_text):
        file_name = self._gen_file_name()
        with open(self.metadata_path, 'a+') as f:
            f.write("|".join([file_name, raw_text.strip(), corrected_text.strip()])+"\n")
        recorder.save_audio(os.path.join(self.record_folder, file_name+'.wav'))
        self._n_record +=1
        self._n_words += len(corrected_text.split(' '))
        self._audio_length += recorder.audio_duration

        self._write_project_file()
        self._restat()
        self.project_updated.emit()

    def _gen_file_name(self) -> str:
        return "{}_{:0>5d}".format(self._record_prefix, self._n_record)

    def _restat(self):
        """ Compute word and sentence count over the text bank and the recorded samples """
        word_stat = dict()
        n_sentence, n_record = 0, 0
        n_word_read, n_word_total = 0, 0

        #Recorded samples
        with open(self.metadata_path, 'r') as f:
            sentences = f.readlines()
        n_sentence += len(sentences)
        n_record = n_sentence
        for sentence in [s.split('|')[2] for s in sentences if len(s) > 0]:
            n_w = len(sentence.split(' '))
            n_word_read += n_w
            n_word_total += n_w
            if n_w not in word_stat.keys():
                word_stat[n_w] = 1
            else:
                word_stat[n_w] += 1
        
        #Text bank
        with open(self.project_base_text, 'r') as f:
            sentences = f.readlines()
        n_sentence += len(sentences)
        for sentence in sentences:
            n_w = len(sentence.split(' '))
            n_word_total += n_w
            if n_w not in word_stat.keys():
                word_stat[n_w] = 1
            else:
                word_stat[n_w] += 1

        self._words_stats = word_stat
        self._n_record = n_record
        self._n_sentence = n_sentence
        self._total_word = n_word_total
        self._n_words = n_word_read

    @property
    def words_stats(self)-> dict:
        return self._words_stats

    @property
    def project_base_text(self) -> str:
        return os.path.join(self._project_folder, "text_bank.txt")

    @property
    def project_manifest(self) -> str:
        return os.path.join(self._project_folder, self._project_name+'.proj')

    @property
    def record_folder(self) -> str:
        return os.path.join(self._project_folder, "audio")

    @property
    def metadata_path(self) -> str:
        return os.path.join(self._project_folder, "metadata.csv")

    @property
    def formated_duration(self) -> str:
        hour, minute, second = 0, 0, self._audio_length
        hour = second // 3600
        second -= hour * 3600
        minute = second // 60
        second -= minute * 60
        return "{:3}h {:2}m {:2}s".format(int(hour), int(minute), int(second))

 