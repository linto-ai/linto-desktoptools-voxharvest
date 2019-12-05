# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rbaraglia/pensieve/home.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(800, 480)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Home)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 147, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_PB = QtWidgets.QPushButton(Home)
        self.open_PB.setObjectName("open_PB")
        self.verticalLayout.addWidget(self.open_PB)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_last_PB = QtWidgets.QPushButton(Home)
        self.open_last_PB.setObjectName("open_last_PB")
        self.horizontalLayout.addWidget(self.open_last_PB)
        self.last_project_label = QtWidgets.QLabel(Home)
        self.last_project_label.setText("")
        self.last_project_label.setAlignment(QtCore.Qt.AlignCenter)
        self.last_project_label.setObjectName("last_project_label")
        self.horizontalLayout.addWidget(self.last_project_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.create_PB = QtWidgets.QPushButton(Home)
        self.create_PB.setObjectName("create_PB")
        self.verticalLayout_2.addWidget(self.create_PB)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 147, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Form"))
        self.open_PB.setText(_translate("Home", "Open Project"))
        self.open_last_PB.setText(_translate("Home", "Open Last Project"))
        self.create_PB.setText(_translate("Home", "Create Project"))
