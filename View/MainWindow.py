import sys
import platform

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from pyqtgraph import PlotWidget

from Ui_MainWindow import Ui_MainWindow
from Ui_Functions import *

from Controller import *
from Controller.Controller import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def moveWindow(event):
            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos()+event.globalPos()-self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

            self.controller.call_view()

        self.ui.frame_title.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)
        self.show()


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())