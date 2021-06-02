# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pyqtgraph import PlotWidget

import logo_rc
import menu_rc
import menu_rc
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.centralwidget)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMaximumSize(QSize(16777215, 50))
        self.frame_title.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title_title = QFrame(self.frame_title)
        self.frame_title_title.setObjectName(u"frame_title_title")
        self.frame_title_title.setFrameShape(QFrame.NoFrame)
        self.frame_title_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_title_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 5, 0, 5)
        self.label_logo = QLabel(self.frame_title_title)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(45, 16777215))
        self.label_logo.setPixmap(QPixmap(u":/resources/logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_logo)

        self.label_title = QLabel(self.frame_title_title)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(22)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(0, 191, 255)")

        self.horizontalLayout_3.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title_title)

        self.frame_title_controls = QFrame(self.frame_title)
        self.frame_title_controls.setObjectName(u"frame_title_controls")
        self.frame_title_controls.setMaximumSize(QSize(80, 16777215))
        self.frame_title_controls.setFrameShape(QFrame.NoFrame)
        self.frame_title_controls.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title_controls)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_title_controls)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(15, 15))
        self.btn_minimize.setMaximumSize(QSize(16, 16))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(14, 132, 32);\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(14, 132, 32, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_title_controls)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(15, 15))
        self.btn_maximize.setMaximumSize(QSize(16, 16))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(249, 155, 17);\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 175, 17);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_title_controls)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(15, 15))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(199, 22, 43);\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(245, 22, 43);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_title_controls)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame_app = QFrame(self.centralwidget)
        self.frame_app.setObjectName(u"frame_app")
        self.frame_app.setStyleSheet(u"background-color: rgb(51, 51, 51);")
        self.frame_app.setFrameShape(QFrame.NoFrame)
        self.frame_app.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_app)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_app)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(50, 0))
        self.frame_menu.setMaximumSize(QSize(50, 16777215))
        self.frame_menu.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_menu.setFrameShape(QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_home = QFrame(self.frame_menu)
        self.frame_menu_home.setObjectName(u"frame_menu_home")
        self.frame_menu_home.setMaximumSize(QSize(16777215, 50))
        self.frame_menu_home.setStyleSheet(u"QFrame  {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgb(0, 191, 255);\n"
"}")
        self.frame_menu_home.setFrameShape(QFrame.NoFrame)
        self.frame_menu_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_menu_home)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_home = QPushButton(self.frame_menu_home)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        self.btn_menu_home.setMaximumSize(QSize(16777215, 50))
        self.btn_menu_home.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u":/resorces/menu/Chart-Axes-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_home.setIcon(icon)
        self.btn_menu_home.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.btn_menu_home)


        self.verticalLayout_2.addWidget(self.frame_menu_home)

        self.frame_menu_new = QFrame(self.frame_menu)
        self.frame_menu_new.setObjectName(u"frame_menu_new")
        self.frame_menu_new.setMaximumSize(QSize(16777215, 50))
        self.frame_menu_new.setStyleSheet(u"QFrame  {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgb(0, 191, 255);\n"
"}")
        self.frame_menu_new.setFrameShape(QFrame.NoFrame)
        self.frame_menu_new.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_menu_new)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_new = QPushButton(self.frame_menu_new)
        self.btn_menu_new.setObjectName(u"btn_menu_new")
        self.btn_menu_new.setMaximumSize(QSize(16777215, 50))
        self.btn_menu_new.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/resorces/menu/Document-Add-01-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_new.setIcon(icon1)
        self.btn_menu_new.setIconSize(QSize(27, 27))

        self.horizontalLayout_8.addWidget(self.btn_menu_new)


        self.verticalLayout_2.addWidget(self.frame_menu_new)

        self.frame_save = QFrame(self.frame_menu)
        self.frame_save.setObjectName(u"frame_save")
        self.frame_save.setMaximumSize(QSize(16777215, 50))
        self.frame_save.setStyleSheet(u"QFrame  {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgb(0, 191, 255);\n"
"}")
        self.frame_save.setFrameShape(QFrame.NoFrame)
        self.frame_save.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_save)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_save = QPushButton(self.frame_save)
        self.btn_menu_save.setObjectName(u"btn_menu_save")
        self.btn_menu_save.setMaximumSize(QSize(16777215, 50))
        self.btn_menu_save.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon2 = QIcon()
        icon2.addFile(u":/resorces/menu/Floppy-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/resorces/menu/Floppy-50.png", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u":/resorces/menu/Floppy-50.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon2.addFile(u":/resorces/menu/Floppy-50.png", QSize(), QIcon.Active, QIcon.Off)
        icon2.addFile(u":/resorces/menu/Floppy-50.png", QSize(), QIcon.Selected, QIcon.Off)
        self.btn_menu_save.setIcon(icon2)
        self.btn_menu_save.setIconSize(QSize(27, 27))

        self.horizontalLayout_9.addWidget(self.btn_menu_save)


        self.verticalLayout_2.addWidget(self.frame_save)

        self.frame_open = QFrame(self.frame_menu)
        self.frame_open.setObjectName(u"frame_open")
        self.frame_open.setMaximumSize(QSize(16777215, 50))
        self.frame_open.setStyleSheet(u"QFrame  {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgb(0, 191, 255);\n"
"}")
        self.frame_open.setFrameShape(QFrame.NoFrame)
        self.frame_open.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_open)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_open = QPushButton(self.frame_open)
        self.btn_menu_open.setObjectName(u"btn_menu_open")
        self.btn_menu_open.setMaximumSize(QSize(16777215, 50))
        self.btn_menu_open.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon3 = QIcon()
        icon3.addFile(u":/resorces/menu/Open-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_open.setIcon(icon3)
        self.btn_menu_open.setIconSize(QSize(27, 27))

        self.horizontalLayout_10.addWidget(self.btn_menu_open)


        self.verticalLayout_2.addWidget(self.frame_open)

        self.frame_filler = QFrame(self.frame_menu)
        self.frame_filler.setObjectName(u"frame_filler")
        self.frame_filler.setStyleSheet(u"QFrame  {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame_filler.setFrameShape(QFrame.NoFrame)
        self.frame_filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_filler)

        self.frame_menu_help = QFrame(self.frame_menu)
        self.frame_menu_help.setObjectName(u"frame_menu_help")
        self.frame_menu_help.setMaximumSize(QSize(16777215, 50))
        self.frame_menu_help.setStyleSheet(u"QFrame  {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgb(0, 191, 255);\n"
"}")
        self.frame_menu_help.setFrameShape(QFrame.NoFrame)
        self.frame_menu_help.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_menu_help)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_help = QPushButton(self.frame_menu_help)
        self.btn_menu_help.setObjectName(u"btn_menu_help")
        self.btn_menu_help.setMaximumSize(QSize(16777215, 50))
        self.btn_menu_help.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon4 = QIcon()
        icon4.addFile(u":/resorces/menu/Help-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_help.setIcon(icon4)
        self.btn_menu_help.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_menu_help)


        self.verticalLayout_2.addWidget(self.frame_menu_help)

        self.frame_menu_exit = QFrame(self.frame_menu)
        self.frame_menu_exit.setObjectName(u"frame_menu_exit")
        self.frame_menu_exit.setMaximumSize(QSize(16777215, 50))
        self.frame_menu_exit.setStyleSheet(u"QFrame  {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgb(0, 191, 255);\n"
"}")
        self.frame_menu_exit.setFrameShape(QFrame.NoFrame)
        self.frame_menu_exit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_menu_exit)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_exit = QPushButton(self.frame_menu_exit)
        self.btn_menu_exit.setObjectName(u"btn_menu_exit")
        self.btn_menu_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_menu_exit.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon5 = QIcon()
        icon5.addFile(u":/resorces/menu/Close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_exit.setIcon(icon5)
        self.btn_menu_exit.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.btn_menu_exit)


        self.verticalLayout_2.addWidget(self.frame_menu_exit)


        self.horizontalLayout_4.addWidget(self.frame_menu)

        self.frame_content = QFrame(self.frame_app)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_graphs = QWidget()
        self.page_graphs.setObjectName(u"page_graphs")
        self.verticalLayout_4 = QVBoxLayout(self.page_graphs)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_graphs_top = QFrame(self.page_graphs)
        self.frame_graphs_top.setObjectName(u"frame_graphs_top")
        self.frame_graphs_top.setFrameShape(QFrame.StyledPanel)
        self.frame_graphs_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_graphs_top)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_model_settings = QFrame(self.frame_graphs_top)
        self.frame_model_settings.setObjectName(u"frame_model_settings")
        self.frame_model_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_model_settings.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_model_settings)

        self.frame_graph_1 = QFrame(self.frame_graphs_top)
        self.frame_graph_1.setObjectName(u"frame_graph_1")
        self.frame_graph_1.setFrameShape(QFrame.NoFrame)
        self.frame_graph_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_graph_1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget = PlotWidget(self.frame_graph_1)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(573, 373))

        self.horizontalLayout_13.addWidget(self.widget)


        self.horizontalLayout_6.addWidget(self.frame_graph_1)


        self.verticalLayout_4.addWidget(self.frame_graphs_top)

        self.frame_graphs_bottom = QFrame(self.page_graphs)
        self.frame_graphs_bottom.setObjectName(u"frame_graphs_bottom")
        self.frame_graphs_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_graphs_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_graphs_bottom)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_graph_phase = QFrame(self.frame_graphs_bottom)
        self.frame_graph_phase.setObjectName(u"frame_graph_phase")
        self.frame_graph_phase.setFrameShape(QFrame.StyledPanel)
        self.frame_graph_phase.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_graph_phase)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_3 = PlotWidget(self.frame_graph_phase)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(573, 373))

        self.horizontalLayout_14.addWidget(self.widget_3)


        self.horizontalLayout_12.addWidget(self.frame_graph_phase)

        self.frame_graph_2 = QFrame(self.frame_graphs_bottom)
        self.frame_graph_2.setObjectName(u"frame_graph_2")
        self.frame_graph_2.setFrameShape(QFrame.StyledPanel)
        self.frame_graph_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_graph_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget_2 = PlotWidget(self.frame_graph_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(573, 373))

        self.horizontalLayout_15.addWidget(self.widget_2)


        self.horizontalLayout_12.addWidget(self.frame_graph_2)


        self.verticalLayout_4.addWidget(self.frame_graphs_bottom)

        self.stackedWidget.addWidget(self.page_graphs)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.stackedWidget.addWidget(self.page_help)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.frame_content)


        self.verticalLayout.addWidget(self.frame_app)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_logo.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"BioModeller", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.btn_menu_home.setText("")
        self.btn_menu_new.setText("")
        self.btn_menu_save.setText("")
        self.btn_menu_open.setText("")
        self.btn_menu_help.setText("")
        self.btn_menu_exit.setText("")
    # retranslateUi

