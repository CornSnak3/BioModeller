from MainWindow import MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import *
from PySide6.QtCore import *

GLOBAL_STATE = 0

class UIFunctions(MainWindow):
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)

            self.ui.btn_maximize.setToolTip("Maximize")

    ## починить перетаскивание

    def uiDefinitions(self):
        # - title
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_menu_exit.clicked.connect(lambda: self.close())



    def returnStatus(self):
        return GLOBAL_STATE
