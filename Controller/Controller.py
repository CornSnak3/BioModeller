# dict = {
#     'a1': 0.1, 'a2': 0.28, 'b1': 0.011, 'b2': 0.03, # фикс (0, 2*x)
#     'time': 50., 'dt': 0.1,
#     't1': 4.4, 't2': 3.4,
#     'x1*': 100.0, 'x1_0': 50.0, 'x2_0': 10.0
# }

from View.MainWindow import MainWindow

class MainController:
    def __init__(self):
        self.view = MainWindow()

    def call_view(self):
        self.view.ui.label_title.text = "Hola"

