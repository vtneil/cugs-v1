import matplotlib as _mpl
from matplotlib import pyplot as _plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from PySide6 import QtCore, QtGui, QtWidgets


_mpl.use('QtAgg')
_plt.style.use('bmh')


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        QtWidgets.QWidget.__init__(self, parent)
        self.__canvas_width = width
        self.__canvas_height = height
        self.__canvas_dpi = dpi
        self.canvas = Canvas(Figure(dpi=self.__canvas_dpi, tight_layout=True))
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
