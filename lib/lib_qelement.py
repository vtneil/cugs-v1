import numpy as _np
import pyqtgraph as _pg
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCharts import QChart, QChartView, QScatterSeries, QValueAxis, QSplineSeries, QLineSeries
from PySide6.QtGui import QColor, QPen, QPainter
# from PySide6.QtCore import Qt


color_r = QColor(255, 0, 0)
color_g = QColor(0, 255, 0)
color_b = QColor(0, 0, 255)

# Change ui QWidgets parent to QWidget
class QChartData:
    global color_r
    global color_g
    global color_b

    def __init__(self, ChartWidget: QWidget, ChartName: str = 'None (None)', *,
                 Color=QColor(255, 255, 255), legend: bool = False, scatter: bool = False, line_type=None,
                 animation=None):
        """
        QGraphicsView Data Object

        :param ChartWidget:
        :param ChartName:
        :param Color:
        :param legend:
        :param scatter:
        :param line_type:
        """
        if line_type is None:
            line_type = []
        self.__legend = legend
        self.__chart_widget = ChartWidget
        self.__chart_name = ChartName
        self.__color = Color
        self.__bool_scatter = scatter
        self.__line_list = list()
        self.__chart_list = list()
        self.__is_first = True

        self.color_r = color_r
        self.color_g = color_g
        self.color_b = color_b

        self.__pen_r = QPen(self.color_r)
        self.__pen_r.setWidth(2)
        self.__pen_g = QPen(self.color_g)
        self.__pen_g.setWidth(2)
        self.__pen_b = QPen(self.color_b)
        self.__pen_b.setWidth(2)
        self.__pen = QPen(self.__color)

        self.__bg_light = QColor(255, 255, 255)
        self.__fg_light = QColor(21, 21, 21)
        self.__grid_light = QColor(230, 230, 230)

        self.__bg_dark = QColor(62, 67, 112)
        self.__fg_dark = QColor(203, 215, 255)
        self.__grid_dark = QColor(46, 49, 82)

        self.__bg = self.__bg_light
        self.__fg = self.__fg_light
        self.__grid = self.__grid_light

        # Chart Layout
        self.__chart_chart = QChart()
        self.__chart_chart.legend().setVisible(self.__legend)
        self.__chart_chart.setTitle(self.__chart_name)
        self.__chart_chart.setBackgroundVisible(True)
        self.__chart_chart.setBackgroundRoundness(4)
        self.__chart_chart.layout().setContentsMargins(0, 0, 0, 0)
        self.__chart_chart.setBackgroundBrush(self.__bg)
        self.__chart_chart.setTitleBrush(self.__fg)
        if animation == 'series':
            self.__chart_chart.setAnimationOptions(QChart.SeriesAnimations)
        elif animation == 'all':
            self.__chart_chart.setAnimationOptions(QChart.AllAnimations)
        else:
            self.__chart_chart.setAnimationOptions(QChart.NoAnimation)

        self.__chart_view = QChartView()
        self.__chart_view.setChart(self.__chart_chart)
        self.__chart_view.setRenderHint(QPainter.Antialiasing)

        self.__chart_layout = QVBoxLayout(self.__chart_widget)
        self.__chart_layout.addWidget(self.__chart_view)

        # Constants and Data
        if line_type:
            for __line_type in line_type:
                if __line_type in ['line', 'spline']:
                    self.__line_list.append(__line_type)
                else:
                    self.__line_list.append('line')
        else:
            self.__line_list.append('line')
        self.__y_len = len(self.__line_list)

        # Chart
        self.__chart_chart.createDefaultAxes()
        self.__x_axis = QValueAxis()
        self.__y_axis = QValueAxis()

        self.__x_max = 1.0
        self.__x_min = 0.0
        self.__y_max = 1.0
        self.__y_min = 0.0

        self.__x_axis.setLabelsBrush(self.__fg)
        self.__x_axis.setGridLineColor(self.__grid)
        self.__x_axis.setGridLineVisible(False)
        self.__y_axis.setLabelsBrush(self.__fg)
        self.__y_axis.setGridLineColor(self.__grid)
        self.__y_axis.setGridLineVisible(False)
        self.updateMinMax()

        self.__chart_chart.setAxisX(self.__x_axis)
        self.__chart_chart.setAxisY(self.__y_axis)

        self.__x_data = None
        self.__y_data = _np.array([], dtype='float')

    def append(self, x_new, *y_new):
        y_arr = _np.array(y_new, dtype='float')[:self.__y_len]
        if not (self.__x_data is not None and self.__y_data.size):
            for __line_type in self.__line_list:
                if __line_type == 'line':
                    self.__chart_list.append(QLineSeries())
                elif __line_type == 'spline':
                    self.__chart_list.append(QSplineSeries())
            if self.__bool_scatter:
                self.__chart_list.append(QScatterSeries())
            for i, __chart in enumerate(self.__chart_list):
                if i == 0:
                    __chart.setPen(self.__pen_r)
                elif i == 1:
                    __chart.setPen(self.__pen_g)
                else:
                    __chart.setPen(self.__pen_b)
                self.__chart_chart.addSeries(__chart)
                __chart.attachAxis(self.__x_axis)
                __chart.attachAxis(self.__y_axis)

        self.__x_data = x_new
        self.__y_data = y_arr

        # Plot only first data in y vector
        for __y, __chart in zip(y_arr, self.__chart_list):
            __chart.append(float(self.__x_data), float(__y))

        if self.__is_first:
            self.__x_min = self.__x_data
            self.__y_min = self.__y_data
            self.__x_max = self.__x_data
            self.__y_max = self.__y_data
            self.__is_first = False
        else:
            self.__x_min = self.selMin(self.__x_min, self.__x_data)
            self.__y_min = self.selMin(self.__y_min, self.__y_data)
            self.__x_max = self.selMax(self.__x_max, self.__x_data)
            self.__y_max = self.selMax(self.__y_max, self.__y_data)
        self.updateMinMax()

        return

    def updateMinMax(self):
        self.__x_axis.setRange(self.__x_min, self.__x_max)
        self.__y_axis.setRange(self.__y_min, self.__y_max)
        return

    def clear(self):
        for __chart in self.__chart_list:
            __chart.clear()
        self.__x_data = 0.0
        self.__y_data = _np.array([], dtype='float')
        self.__x_min = 0.0
        self.__x_max = 1.0
        self.__y_min = 0.0
        self.__y_max = 1.0
        self.updateMinMax()
        return

    def pop(self):
        if self.__x_data.size > 0:
            for __y, __chart in zip(self.__y_data, self.__chart_list):
                __chart.remove(self.__x_data, __y)

            self.__x_min = self.selMin(self.__x_min, self.__x_data)
            self.__y_min = self.selMin(self.__y_min, self.__y_data)
            self.__x_max = self.selMax(self.__x_max, self.__x_data)
            self.__y_max = self.selMax(self.__y_max, self.__y_data)
            self.updateMinMax()
        return

    def setTitle(self, value, unit: str):
        self.__chart_chart.setTitle('{} ({})'.format(value, unit))

    @staticmethod
    def selMin(a, b):
        if a < b:
            return a
        else:
            return b

    @staticmethod
    def selMax(a, b):
        if a > b:
            return a
        else:
            return b

class PyQtGraphData:
    def __init__(self, ChartWidget: QWidget, ChartName: str = 'None (None)', *,
                 legend: bool = False):
        """
        PyQtGraph Data Object
        """
        self.__chart_widget = ChartWidget
        self.__chart_view = _pg.PlotWidget()
        self.__chart_layout = QVBoxLayout(self.__chart_widget)
        self.__chart_layout.addWidget(self.__chart_view)


    def append(self, x_new, *y_new):
        return

    def updateMinMax(self):
        return

    def clear(self):
        return

    def pop(self):
        return

    def setTitle(self, value, unit: str):
        return

class QTableData:
    def __init__(self, table: QTableWidget):
        """
        A QTableWidget Object containing data.
        """
        self.table = table
        self.data_count = 0

    def replaceVector(self, data_dict: dict):
        self.table.setRowCount(len(data_dict))
        for r, (k, v) in enumerate(data_dict.items()):
            self.table.setItem(r, 0, QTableWidgetItem(str(k)))
            self.table.setItem(r, 1, QTableWidgetItem(str(v)))
        return

    def appendTable(self, data_dict: dict):
        if self.data_count >= 1000:
            self.clear()
        self.table.setRowCount(self.data_count + 1)
        self.table.setColumnCount(len(data_dict))
        for c, (k, v) in enumerate(data_dict.items()):
            self.table.setHorizontalHeaderItem(c, QTableWidgetItem(str(k)))
            __v = str(v)
            self.table.setItem(self.data_count, c, QTableWidgetItem(__v))
        self.data_count += 1
        QAbstractItemView.scrollToBottom(self.table)
        return

    def clear(self):
        self.table.setRowCount(0)
        self.data_count = 0
        return

    def pop(self):
        self.data_count -= 1
        self.table.setRowCount(self.data_count)
        return