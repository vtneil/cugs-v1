from PySide6.QtCharts import QChart, QChartView, QScatterSeries, QValueAxis, QSplineSeries, QLineSeries
from PySide6.QtGui import QColor, QPen, QPainter


class PyQtCharts:
    def __init__(self, ChartLayout: QChartView, ChartName='None (none)', UseScatter=False, UseSpline=True,
                 Color=QColor(255, 255, 255), LegendVisible=False) -> None:
        """
        Create Custom QChart and Data Attributes Set Class
        :param ChartLayout:
        :param ChartName:
        :param UseScatter:
        :param UseSpline:
        :param Color:
        :param LegendVisible:
        """
        self.chart_layout = ChartLayout
        self.chart_chart = QChart()
        self.scatter_series = QScatterSeries()
        self.chart_chart.createDefaultAxes()
        self.x_axis = QValueAxis()
        self.y_axis = QValueAxis()

        self.legend_visible = LegendVisible
        self.chart_name = ChartName
        self.use_scatter = UseScatter
        self.use_spline = UseSpline

        self.is_dark = False
        self.is_light = not self.is_dark
        self.platform_name = ''

        self.x_data = []
        self.y_data = []
        self.y_alt1 = []
        self.y_alt2 = []
        self.x_new = 0
        self.y_new = 0
        self.y_new1 = 0
        self.y_new2 = 0
        self.x_min = 0
        self.x_max = 10
        self.y_min = 0
        self.y_max = 10
        self.y_min1 = 0
        self.y_max1 = 1
        self.y_min2 = 0
        self.y_max2 = 1

        self.color_r = QColor(255, 0, 0)
        self.color_g = QColor(0, 255, 0)
        self.color_b = QColor(0, 0, 255)
        self.color = Color

        self.pen_r = QPen(self.color_r)
        self.pen_r.setWidth(2)
        self.pen_g = QPen(self.color_g)
        self.pen_g.setWidth(2)
        self.pen_b = QPen(self.color_b)
        self.pen_b.setWidth(2)
        self.pen = QPen(self.color)

        self.bg_light = QColor(255, 255, 255)
        self.fg_light = QColor(21, 21, 21)
        self.grid_light = QColor(230, 230, 230)

        self.bg_dark = QColor(62, 67, 112)
        self.fg_dark = QColor(203, 215, 255)
        self.grid_dark = QColor(46, 49, 82)

        self.bg = self.bg_dark
        self.fg = self.fg_dark
        self.grid = self.grid_dark

        self.chart_layout.setRenderHint(QPainter.Antialiasing)
        self.chart_chart.legend().setVisible(self.legend_visible)
        self.chart_chart.setAnimationOptions(QChart.SeriesAnimations)
        # self.chart_chart.setAnimationOptions(QChart.AllAnimations)
        self.chart_chart.setTitle(self.chart_name)
        self.chart_chart.setBackgroundVisible(True)
        self.chart_chart.setBackgroundRoundness(12)
        self.chart_chart.layout().setContentsMargins(0, 0, 0, 0)

        self.chart_chart.setBackgroundBrush(self.bg)
        self.chart_chart.setTitleBrush(self.fg)
        self.x_axis.setLabelsBrush(self.fg)
        self.x_axis.setGridLineColor(self.grid)
        self.x_axis.setGridLineVisible(False)
        self.y_axis.setLabelsBrush(self.fg)
        self.y_axis.setGridLineColor(self.grid)
        self.y_axis.setGridLineVisible(False)

        self.x_axis.setRange(self.x_min, self.x_max)
        self.y_axis.setRange(min(self.y_min, self.y_min1, self.y_min2), max(self.y_max, self.y_max1, self.y_max2))

        if self.use_spline:
            self.chart = QSplineSeries()
            self.chart1 = QSplineSeries()
            self.chart2 = QSplineSeries()
        else:
            self.chart = QLineSeries()
            self.chart1 = QLineSeries()
            self.chart2 = QLineSeries()

        self.chart.setPen(self.pen_r)
        self.chart1.setPen(self.pen_g)
        self.chart2.setPen(self.pen_b)

        self.chart_chart.addSeries(self.chart)
        self.chart_chart.addSeries(self.chart1)
        self.chart_chart.addSeries(self.chart2)
        self.chart_chart.setAxisX(self.x_axis)
        self.chart_chart.setAxisY(self.y_axis)

        if self.use_scatter:
            self.scatter_series.setColor(self.color)
            self.scatter_series.setMarkerSize(8)
            self.chart_chart.addSeries(self.scatter_series)

        self.chart.attachAxis(self.x_axis)
        self.chart.attachAxis(self.y_axis)
        self.chart1.attachAxis(self.x_axis)
        self.chart1.attachAxis(self.y_axis)
        self.chart2.attachAxis(self.x_axis)
        self.chart2.attachAxis(self.y_axis)
        self.scatter_series.attachAxis(self.x_axis)
        self.scatter_series.attachAxis(self.y_axis)

        self.chart_layout.setChart(self.chart_chart)

    def updateChart(self, x_new, y_new, y_new1=None, y_new2=None):
        self.x_new = x_new
        self.y_new = y_new
        self.y_new1 = y_new1
        self.y_new2 = y_new2

        self.chart.append(float(self.x_new), float(self.y_new))
        self.x_data.append(float(self.x_new))
        self.y_data.append(float(self.y_new))

        if self.y_new1 is not None:
            self.chart1.append(float(self.x_new), float(self.y_new1))
            self.y_alt1.append(float(self.y_new1))

        if self.y_new2 is not None:
            self.chart2.append(float(self.x_new), float(self.y_new2))
            self.y_alt2.append(float(self.y_new2))

        if self.use_scatter:
            self.scatter_series.append(float(self.x_new), float(self.y_new))

        self.updateMinMax()

        self.chart_layout.setChart(self.chart_chart)

    def updateMinMax(self) -> None:
        """
        Update minimum and maximum value of chart

        :return:
        """
        self.x_axis.setRange(min(self.x_data), max(self.x_data) + 0.2 * abs(max(self.x_data)))
        self.y_axis.setRange(
            min(self.y_data + self.y_alt1 + self.y_alt2) - 0.2 * abs(min(self.y_data + self.y_alt1 + self.y_alt2)),
            max(self.y_data + self.y_alt1 + self.y_alt2) + 0.2 * abs(max(self.y_data + self.y_alt1 + self.y_alt2)))

    def clearChart(self) -> None:
        """
        Clear chart

        :return:
        """
        self.chart.clear()
        self.chart1.clear()
        self.chart2.clear()
        self.scatter_series.clear()

        self.chart_layout.setChart(self.chart_chart)

    def popChart(self) -> None:
        """
        Remove latest data from the chart

        :return:
        """
        if len(self.x_data) > 1:
            self.chart.remove(self.x_new, self.y_new)
            self.scatter_series.remove(self.x_new, self.y_new)

            if self.y_new1 is not None:
                self.chart1.remove(self.x_new, self.y_new1)

            if self.y_new2 is not None:
                self.chart2.remove(self.x_new, self.y_new2)

            self.x_data.pop()
            self.x_new = self.x_data[len(self.x_data) - 1]

        if len(self.y_data) > 1:
            self.y_data.pop()
            self.y_new = self.y_data[len(self.y_data) - 1]

        if len(self.y_alt1) > 1:
            self.y_alt1.pop()
            self.y_new1 = self.y_alt1[len(self.y_alt1) - 1]

        if len(self.y_alt2) > 1:
            self.y_alt2.pop()
            self.y_new2 = self.y_alt2[len(self.y_alt2) - 1]

        if len(self.x_data) > 1:
            self.updateMinMax()
            pass

        return


if __name__ == '__main__':
    pass
