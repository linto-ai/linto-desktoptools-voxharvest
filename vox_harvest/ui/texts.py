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
        self._load_text_stats()

        #CONNECT
        self.ui.add_raw_PB.clicked.connect(self._on_add_raw_clicked)
        self.ui.add_formated_PB.clicked.connect(self._on_add_formated_clicked)
        self._project.project_updated.connect(self._on_project_updated)

    def _load_text_stats(self):
        self.ui.sentence_count_SP.setValue(self._project._n_sentence)
        self.ui.word_count_SP.setValue(self._project._total_word)

        stats = self._project.words_stats
        min_w = min([v for v in stats.keys()])
        max_w = max([v for v in stats.keys()])
        avg_w = 0
        c = 0
        for k in stats.keys():
            avg_w += stats[k] * k
            c += stats[k]
        avg_w = int(avg_w / c)
        self.ui.avg_SP.setValue(avg_w)
        self.ui.min_SP.setValue(min_w)
        self.ui.max_SP.setValue(max_w)

        self._load_graph(stats, min_w, max_w)

    def _load_graph(self, stats, min_w, max_w):
        if self.ui.histo_widget.layout() is None:
            layout = QtWidgets.QVBoxLayout()
            self.ui.histo_widget.setLayout(layout)
            chart = QtChart.QChart()
            chart.setBackgroundBrush(QtGui.QBrush(self.palette().color(self.backgroundRole())))
            self._chart_view = QtChart.QChartView(chart)
            layout.addWidget(self._chart_view)
            self._serie = QtChart.QLineSeries()
            self._serie.setName("Word count")
            chart.addSeries(self._serie)
            chart.createDefaultAxes()
            self._chart_view.show()

        self._serie.clear()
        max_s = max([v for v in stats.values()])
        for i in range(min_w, max_w):
            self._serie.append(i, stats.get(i, 0))
        self._chart_view.chart().axisX().setRange(min_w -1, max_w + 1)
        self._chart_view.chart().axisY().setRange(0, max_s + 1)


    def _on_project_updated(self):
        self._load_text_stats()

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
        res = QtWidgets.QFileDialog.getOpenFileName(self, "Select a text file", "", "All File (*.*)")[0]
        if len(res) > 0:
            with open(res, 'r') as f:
                sentences = f.readlines()
            self._project.add_text([s.strip() for s in sentences])

        
    
