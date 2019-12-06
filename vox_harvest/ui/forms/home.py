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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.banner_LB = QtWidgets.QLabel(Home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.banner_LB.sizePolicy().hasHeightForWidth())
        self.banner_LB.setSizePolicy(sizePolicy)
        self.banner_LB.setMinimumSize(QtCore.QSize(300, 150))
        self.banner_LB.setObjectName("banner_LB")
        self.horizontalLayout_2.addWidget(self.banner_LB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Home)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.create_PB = QtWidgets.QPushButton(Home)
        self.create_PB.setObjectName("create_PB")
        self.verticalLayout_2.addWidget(self.create_PB)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 147, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Form"))
        self.banner_LB.setText(_translate("Home", "Linagora_lab"))
        self.open_PB.setText(_translate("Home", "Open Project"))
        self.open_last_PB.setText(_translate("Home", "Open Last Project"))
        self.create_PB.setText(_translate("Home", "Create Project"))
