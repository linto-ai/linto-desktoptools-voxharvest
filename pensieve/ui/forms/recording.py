# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rbaraglia/pensieve/recording_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recording_widget(object):
    def setupUi(self, recording_widget):
        recording_widget.setObjectName("recording_widget")
        recording_widget.resize(748, 468)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(recording_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sentence_index_SP = QtWidgets.QSpinBox(recording_widget)
        self.sentence_index_SP.setReadOnly(True)
        self.sentence_index_SP.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sentence_index_SP.setObjectName("sentence_index_SP")
        self.horizontalLayout.addWidget(self.sentence_index_SP)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(recording_widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.sentence_TE = QtWidgets.QTextBrowser(recording_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sentence_TE.sizePolicy().hasHeightForWidth())
        self.sentence_TE.setSizePolicy(sizePolicy)
        self.sentence_TE.setReadOnly(False)
        self.sentence_TE.setObjectName("sentence_TE")
        self.verticalLayout.addWidget(self.sentence_TE)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.next_PB = QtWidgets.QPushButton(recording_widget)
        self.next_PB.setObjectName("next_PB")
        self.horizontalLayout.addWidget(self.next_PB)
        self.skip_PB = QtWidgets.QPushButton(recording_widget)
        self.skip_PB.setObjectName("skip_PB")
        self.horizontalLayout.addWidget(self.skip_PB)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(recording_widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.signal_widget = QtWidgets.QWidget(recording_widget)
        self.signal_widget.setObjectName("signal_widget")
        self.verticalLayout_2.addWidget(self.signal_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.record_PB = QtWidgets.QPushButton(recording_widget)
        self.record_PB.setObjectName("record_PB")
        self.horizontalLayout_2.addWidget(self.record_PB)
        self.stop_PB = QtWidgets.QPushButton(recording_widget)
        self.stop_PB.setEnabled(False)
        self.stop_PB.setObjectName("stop_PB")
        self.horizontalLayout_2.addWidget(self.stop_PB)
        self.listen_PB = QtWidgets.QPushButton(recording_widget)
        self.listen_PB.setEnabled(False)
        self.listen_PB.setObjectName("listen_PB")
        self.horizontalLayout_2.addWidget(self.listen_PB)
        self.validate_PB = QtWidgets.QPushButton(recording_widget)
        self.validate_PB.setEnabled(False)
        self.validate_PB.setObjectName("validate_PB")
        self.horizontalLayout_2.addWidget(self.validate_PB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(recording_widget)
        QtCore.QMetaObject.connectSlotsByName(recording_widget)

    def retranslateUi(self, recording_widget):
        _translate = QtCore.QCoreApplication.translate
        recording_widget.setWindowTitle(_translate("recording_widget", "Form"))
        self.label.setText(_translate("recording_widget", "Text to read:"))
        self.next_PB.setText(_translate("recording_widget", "Next"))
        self.skip_PB.setText(_translate("recording_widget", "Skip"))
        self.record_PB.setText(_translate("recording_widget", "Record"))
        self.stop_PB.setText(_translate("recording_widget", "Stop"))
        self.listen_PB.setText(_translate("recording_widget", "Listen"))
        self.validate_PB.setText(_translate("recording_widget", "Validate and next"))
