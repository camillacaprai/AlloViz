# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alloviz_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 725)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.atomselEdit = QtWidgets.QLineEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atomselEdit.sizePolicy().hasHeightForWidth())
        self.atomselEdit.setSizePolicy(sizePolicy)
        self.atomselEdit.setObjectName("atomselEdit")
        self.verticalLayout_8.addWidget(self.atomselEdit)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setEnabled(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.methodTree = QtWidgets.QTreeWidget(self.groupBox)
        self.methodTree.setColumnCount(2)
        self.methodTree.setObjectName("methodTree")
        self.methodTree.headerItem().setText(0, "1")
        self.methodTree.headerItem().setText(1, "2")
        self.verticalLayout_4.addWidget(self.methodTree)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkbox_GPCR_Interhelix = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_GPCR_Interhelix.setObjectName("checkbox_GPCR_Interhelix")
        self.gridLayout_2.addWidget(self.checkbox_GPCR_Interhelix, 4, 0, 1, 3)
        self.checkbox_No_Sequence_Neighbors = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_No_Sequence_Neighbors.setObjectName("checkbox_No_Sequence_Neighbors")
        self.gridLayout_2.addWidget(self.checkbox_No_Sequence_Neighbors, 2, 0, 1, 1)
        self.edit_GetContacts_threshold = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_GetContacts_threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_GetContacts_threshold.setObjectName("edit_GetContacts_threshold")
        self.gridLayout_2.addWidget(self.edit_GetContacts_threshold, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.edit_Interresidue_distance = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_Interresidue_distance.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_Interresidue_distance.setObjectName("edit_Interresidue_distance")
        self.gridLayout_2.addWidget(self.edit_Interresidue_distance, 3, 1, 1, 1)
        self.checkbox_Spatially_distant = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_Spatially_distant.setObjectName("checkbox_Spatially_distant")
        self.gridLayout_2.addWidget(self.checkbox_Spatially_distant, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.checkbox_GetContacts_edges = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_GetContacts_edges.setObjectName("checkbox_GetContacts_edges")
        self.gridLayout_2.addWidget(self.checkbox_GetContacts_edges, 1, 0, 1, 1)
        self.edit_Sequence_Neighbor_distance = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_Sequence_Neighbor_distance.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_Sequence_Neighbor_distance.setObjectName("edit_Sequence_Neighbor_distance")
        self.gridLayout_2.addWidget(self.edit_Sequence_Neighbor_distance, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 200)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.anEdgeBtwCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.anEdgeBtwCheck.setChecked(True)
        self.anEdgeBtwCheck.setObjectName("anEdgeBtwCheck")
        self.gridLayout.addWidget(self.anEdgeBtwCheck, 1, 0, 1, 1)
        self.anNodeBtwCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.anNodeBtwCheck.setObjectName("anNodeBtwCheck")
        self.gridLayout.addWidget(self.anNodeBtwCheck, 1, 1, 1, 1)
        self.anEdgeRawCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.anEdgeRawCheck.setObjectName("anEdgeRawCheck")
        self.gridLayout.addWidget(self.anEdgeRawCheck, 4, 0, 1, 2)
        self.anEdgeCurrentCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.anEdgeCurrentCheck.setObjectName("anEdgeCurrentCheck")
        self.gridLayout.addWidget(self.anEdgeCurrentCheck, 3, 0, 1, 1)
        self.anNodeCurrentCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.anNodeCurrentCheck.setObjectName("anNodeCurrentCheck")
        self.gridLayout.addWidget(self.anNodeCurrentCheck, 3, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.edit_hide_fraction = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_hide_fraction.sizePolicy().hasHeightForWidth())
        self.edit_hide_fraction.setSizePolicy(sizePolicy)
        self.edit_hide_fraction.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_hide_fraction.setObjectName("edit_hide_fraction")
        self.gridLayout_3.addWidget(self.edit_hide_fraction, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.runButton = QtWidgets.QPushButton(self.widget)
        self.runButton.setEnabled(False)
        self.runButton.setObjectName("runButton")
        self.verticalLayout_7.addWidget(self.runButton)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_7.addWidget(self.progressBar)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.historyWidget = QtWidgets.QListWidget(self.widget_2)
        self.historyWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.historyWidget.setObjectName("historyWidget")
        self.verticalLayout_9.addWidget(self.historyWidget)
        self.btnDelta = QtWidgets.QPushButton(self.widget_2)
        self.btnDelta.setEnabled(False)
        self.btnDelta.setFlat(False)
        self.btnDelta.setObjectName("btnDelta")
        self.verticalLayout_9.addWidget(self.btnDelta)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAlloViz_Homepage = QtWidgets.QAction(MainWindow)
        self.actionAlloViz_Homepage.setObjectName("actionAlloViz_Homepage")
        self.actionCitation = QtWidgets.QAction(MainWindow)
        self.actionCitation.setObjectName("actionCitation")
        self.actionAlloViz_Source = QtWidgets.QAction(MainWindow)
        self.actionAlloViz_Source.setObjectName("actionAlloViz_Source")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menu_Help.addAction(self.actionAlloViz_Homepage)
        self.menu_Help.addAction(self.actionAlloViz_Source)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionCitation)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlloViz GUI"))
        self.groupBox_4.setTitle(_translate("MainWindow", "1. Select atoms to include (top molecule)"))
        self.label_2.setText(_translate("MainWindow", "VMD atom selection"))
        self.atomselEdit.setText(_translate("MainWindow", "protein and noh"))
        self.groupBox.setTitle(_translate("MainWindow", "2. Network construction method"))
        self.groupBox_2.setTitle(_translate("MainWindow", "3. Filter"))
        self.checkbox_GPCR_Interhelix.setText(_translate("MainWindow", "Interhelix contacts (GPCRs only)"))
        self.checkbox_No_Sequence_Neighbors.setText(_translate("MainWindow", "Minimum sequence distance"))
        self.edit_GetContacts_threshold.setText(_translate("MainWindow", "0.5"))
        self.label.setText(_translate("MainWindow", "Threshold"))
        self.edit_Interresidue_distance.setText(_translate("MainWindow", "10"))
        self.checkbox_Spatially_distant.setText(_translate("MainWindow", "Minumum spatial distance"))
        self.label_3.setText(_translate("MainWindow", "[0-1]"))
        self.label_5.setText(_translate("MainWindow", "Å"))
        self.label_6.setText(_translate("MainWindow", "Criteria"))
        self.checkbox_GetContacts_edges.setText(_translate("MainWindow", "Minimum GetContacts frequency"))
        self.edit_Sequence_Neighbor_distance.setText(_translate("MainWindow", "5"))
        self.label_4.setText(_translate("MainWindow", "AAs"))
        self.groupBox_3.setTitle(_translate("MainWindow", "4. Analysis"))
        self.anEdgeBtwCheck.setText(_translate("MainWindow", "Edge betweenness"))
        self.anNodeBtwCheck.setText(_translate("MainWindow", "&Node betweenness"))
        self.anEdgeRawCheck.setText(_translate("MainWindow", "Raw edge &values"))
        self.anEdgeCurrentCheck.setText(_translate("MainWindow", "Edge current flow betw."))
        self.anNodeCurrentCheck.setText(_translate("MainWindow", "Node current flow betw."))
        self.groupBox_5.setTitle(_translate("MainWindow", "5. Visualize"))
        self.edit_hide_fraction.setText(_translate("MainWindow", "50"))
        self.label_8.setText(_translate("MainWindow", "Only visualize values above"))
        self.label_9.setText(_translate("MainWindow", "% of maximum"))
        self.runButton.setText(_translate("MainWindow", "Compute and Visualize"))
        self.label_7.setText(_translate("MainWindow", "History"))
        self.btnDelta.setText(_translate("MainWindow", "Compute Δ network"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionAbout.setText(_translate("MainWindow", "A&bout..."))
        self.actionAlloViz_Homepage.setText(_translate("MainWindow", "&AlloViz Homepage..."))
        self.actionCitation.setText(_translate("MainWindow", "&Citation..."))
        self.actionAlloViz_Source.setText(_translate("MainWindow", "AlloViz Source..."))