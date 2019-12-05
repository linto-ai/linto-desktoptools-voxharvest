import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

from ui.forms.recording import Ui_recording_widget

class Record_Widget(QtWidgets.QWidget):
    def __init__(self, project):
        super().__init__()
        self.ui = Ui_recording_widget()
        self.ui.setupUi(self)
        self._init_chart()
    
    def _init_chart(self):
        if self.ui.signal_widget.layout() is None:
            layout = QtWidgets.QHBoxLayout()
            self._chart = QtChart.QChart()
            self._chart.createDefaultAxes()
            
            self._serie = QtChart.QLineSeries()
            self._serie.setName("signal")
            self._chart.addSeries(self._serie)

            self._chart_view = QtChart.QChartView(self._chart)
            self._chart_view.show()
            layout.addWidget(self._chart_view)
            self.ui.signal_widget.setLayout(layout)

            #self._chart_view.chart().axisY().setRange(np.iinfo(np.int16).min, np.iinfo(np.int16).max)