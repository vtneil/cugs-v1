# # import sys as _sys
# import numpy as _np
# import matplotlib as _mpl
# import threading as _threading
# import gui.mplwidget as mplwidget
# from typing import Union as _Union
# from matplotlib import pyplot as _plt
# from matplotlib import animation as _animation
# from matplotlib.figure import Figure as _Figure
# from PySide6.QtWidgets import QMainWindow as _QMainWindow
# from PySide6.QtWidgets import QApplication as _QApplication
# from PySide6.QtWidgets import QVBoxLayout as _QVBoxLayout
# from PySide6.QtWidgets import QWidget as _QWidget
#
# _mpl.use('QtAgg')
# _plt.style.use('bmh')
#
#
# # _plt.style.use('dark_background')
#
#
# class MplDataClass:
#     def __init__(self, use_np: bool = False):
#         """
#         MplDataClass (Upcoming)
#
#         :param use_np:
#         """
#         self.use_np = use_np
#         if self.use_np:
#             self.x_data = _np.array([])
#             self.y_data = _np.array([])
#         else:
#             self.x_data = []
#             self.y_data = []
#
#     def appendX(self, to_append):
#         if (isinstance(self.x_data, _np.ndarray)):
#             self.x_data = _np.append(self.x_data, to_append)
#         else:
#             self.x_data.append(to_append)
#         return
#
#     def appendY(self, *to_append):
#         for i, __arr, __a in enumerate(zip(self.y_data, to_append)):
#             if (isinstance(self.y_data, _np.ndarray)):
#                 self.y_data[i] = _np.append(__arr, __a)
#             else:
#                 self.y_data[i].append(__a)
#         return
#
#
#
#
# class MplDataFetcher(_threading.Thread):
#     """
#     MplDataFetcher (Upcoming)
#
#     """
#
#     def __init__(self, DataClass=MplDataClass, interval=500):
#         _threading.Thread.__init__(self)
#         self.__data_class = DataClass
#         self.__interval = interval / 1000
#
#     def run(self):
#         try:
#             while True:
#                 pass
#         except KeyboardInterrupt:
#             pass
#
#
# class MplCanvasQt(mplwidget.MplWidget):
#     def __init__(self, parent=None, width=5, height=4, dpi=100, use_np: bool = False, reduce_func=None) -> None:
#         """
#         Matplotlib class for PySide6 (Upcoming)
#
#         :param parent: parent
#         :param width: mpl width
#         :param height: mpl height
#         :param dpi: mpl dpi
#         """
#         self.__canvas_width = width
#         self.__canvas_height = height
#         self.__canvas_dpi = dpi
#         self.__reduce_func = reduce_func
#         self.__use_np = use_np
#
#         mplwidget.MplWidget.__init__(self, parent, self.__canvas_width, self.__canvas_height, self.__canvas_dpi)
#
#     def plotAll(self, data_x: _Union[list, _np.ndarray], data_y: _Union[list, _np.ndarray], mode: str = None):
#         if mode:
#             self.canvas.axes.plot(data_x, data_y, mode)
#         else:
#             self.canvas.axes.plot(data_x, data_y)
#
#     def updatePlot(self, data_x: _Union[list, _np.ndarray], data_y: _Union[list, _np.ndarray]):
#         self.clearCanvas()
#         self.plotAll(data_x, data_y, 'r')
#         self.canvas.axes.draw()
#
#     def clearCanvas(self):
#         self.canvas.axes.cla()
#
#
# if __name__ == '__main__':
#     mplcli = MplCanvasCli('xxx')
#     mplcli.updatePlot(_np.array([1, 2, 3, 4, 5]), _np.array([3, 5, 8, 9, 1]))
#     # _ = input()
