# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StandardWindow.ui'
#
# Created: Wed Jul 15 01:11:07 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1341, 852)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.OpenGlPanel = QtGui.QHBoxLayout()
        self.OpenGlPanel.setObjectName(_fromUtf8("OpenGlPanel"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.OpenGlPanel.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.OpenGlPanel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.importFileButton = QtGui.QPushButton(self.centralwidget)
        self.importFileButton.setObjectName(_fromUtf8("importFileButton"))
        self.verticalLayout_2.addWidget(self.importFileButton)
        self.printerSettingsButton = QtGui.QPushButton(self.centralwidget)
        self.printerSettingsButton.setObjectName(_fromUtf8("printerSettingsButton"))
        self.verticalLayout_2.addWidget(self.printerSettingsButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.UpPosButton = QtGui.QPushButton(self.centralwidget)
        self.UpPosButton.setObjectName(_fromUtf8("UpPosButton"))
        self.verticalLayout_6.addWidget(self.UpPosButton)
        self.DownPosButton = QtGui.QPushButton(self.centralwidget)
        self.DownPosButton.setObjectName(_fromUtf8("DownPosButton"))
        self.verticalLayout_6.addWidget(self.DownPosButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.N = QtGui.QLineEdit(self.centralwidget)
        self.N.setObjectName(_fromUtf8("N"))
        self.horizontalLayout_3.addWidget(self.N)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.StartPosButton = QtGui.QPushButton(self.centralwidget)
        self.StartPosButton.setObjectName(_fromUtf8("StartPosButton"))
        self.verticalLayout_4.addWidget(self.StartPosButton)
        self.EndPosButton = QtGui.QPushButton(self.centralwidget)
        self.EndPosButton.setObjectName(_fromUtf8("EndPosButton"))
        self.verticalLayout_4.addWidget(self.EndPosButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.SlicingButton = QtGui.QPushButton(self.centralwidget)
        self.SlicingButton.setObjectName(_fromUtf8("SlicingButton"))
        self.verticalLayout_5.addWidget(self.SlicingButton)
        self.BoundingBoxButton = QtGui.QPushButton(self.centralwidget)
        self.BoundingBoxButton.setObjectName(_fromUtf8("BoundingBoxButton"))
        self.verticalLayout_5.addWidget(self.BoundingBoxButton)
        self.CenterButton = QtGui.QPushButton(self.centralwidget)
        self.CenterButton.setObjectName(_fromUtf8("CenterButton"))
        self.verticalLayout_5.addWidget(self.CenterButton)
        self.MeshButton = QtGui.QPushButton(self.centralwidget)
        self.MeshButton.setObjectName(_fromUtf8("MeshButton"))
        self.verticalLayout_5.addWidget(self.MeshButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.StartPrintButton = QtGui.QPushButton(self.centralwidget)
        self.StartPrintButton.setAutoDefault(True)
        self.StartPrintButton.setDefault(False)
        self.StartPrintButton.setObjectName(_fromUtf8("StartPrintButton"))
        self.horizontalLayout_4.addWidget(self.StartPrintButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionPrinter_Settings = QtGui.QAction(MainWindow)
        self.actionPrinter_Settings.setObjectName(_fromUtf8("actionPrinter_Settings"))
        self.actionPrinter_Settings_2 = QtGui.QAction(MainWindow)
        self.actionPrinter_Settings_2.setObjectName(_fromUtf8("actionPrinter_Settings_2"))
        self.actionFile_Import = QtGui.QAction(MainWindow)
        self.actionFile_Import.setObjectName(_fromUtf8("actionFile_Import"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.importFileButton.setText(_translate("MainWindow", "Import File", None))
        self.printerSettingsButton.setText(_translate("MainWindow", "Printer Settings", None))
        self.label.setText(_translate("MainWindow", "Stepper Motor Movement", None))
        self.UpPosButton.setText(_translate("MainWindow", "Up by N Steps", None))
        self.DownPosButton.setText(_translate("MainWindow", "Down by N Steps", None))
        self.N.setToolTip(_translate("MainWindow", "<html><head/><body><p>N=</p></body></html>", None))
        self.N.setText(_translate("MainWindow", "10", None))
        self.StartPosButton.setText(_translate("MainWindow", "to Start Position", None))
        self.EndPosButton.setText(_translate("MainWindow", "to End Position", None))
        self.label_2.setText(_translate("MainWindow", "Editing Options", None))
        self.SlicingButton.setText(_translate("MainWindow", "slicer preview", None))
        self.BoundingBoxButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>This SLA printer prints from the bottom up - the 3D model has to have its flattest surface on top.</p></body></html>", None))
        self.BoundingBoxButton.setText(_translate("MainWindow", "bounding box", None))
        self.CenterButton.setText(_translate("MainWindow", "center", None))
        self.MeshButton.setText(_translate("MainWindow", "mesh", None))
        self.StartPrintButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>opens the Printing Dialogue</p></body></html>", None))
        self.StartPrintButton.setText(_translate("MainWindow", "Start Printing!", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))
        self.actionPrinter_Settings.setText(_translate("MainWindow", "Printer Settings", None))
        self.actionPrinter_Settings_2.setText(_translate("MainWindow", "Printer Settings", None))
        self.actionFile_Import.setText(_translate("MainWindow", "File Import", None))

