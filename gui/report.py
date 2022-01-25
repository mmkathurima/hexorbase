# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_reports_dialog(object):
    def setupUi(self, reports_dialog):
        reports_dialog.setObjectName("reports_dialog")
        reports_dialog.resize(298, 55)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(reports_dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(reports_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(278, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(reports_dialog)
        QtCore.QMetaObject.connectSlotsByName(reports_dialog)

    def retranslateUi(self, reports_dialog):
        reports_dialog.setWindowTitle(QtCore.QCoreApplication.translate("reports_dialog", "Generating Report ( 50% )", None))
        self.progressBar.setFormat(QtCore.QCoreApplication.translate("reports_dialog", "%p%", "df"))

