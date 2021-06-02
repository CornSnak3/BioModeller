import sys
import platform
import numpy as np
import pyqtgraph as pg

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from pyqtgraph import PlotWidget

from Model.LotkaVolterra import LotkaVolterra
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

        pg.setConfigOptions(antialias=True)
        self.ui.frame_title.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)
        self.show()

        params = {
                'a1': 0.9, 'a2': 0.7, 'b1': 0.0061, 'b2': 0.0021,
                'time': 30., 'dt': 0.1,
                't1': 1.3, 't2': 1.2,
                'x1*': 100.0, 'x1_0': 20.0, 'x2_0': 10.0
        }

        t = np.arange(0, params['time'], params['dt'])
        lv = LotkaVolterra(params)
        lv.euler()
        self.ui.widget.setBackground('#777')
        self.ui.widget.plot(t, lv.x1, pen=pg.mkPen(color='r', width=1.5))
        self.ui.widget.plot(t, lv.x2, pen=pg.mkPen(color='b', width=1.5))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())