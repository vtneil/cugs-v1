import sys
import lib as ilib
import gui as guilib
# import numpy as np
from lib import Log
# from typing import Union as _Union
from PySide6.QtWidgets import QApplication, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor


class ProgFullStackGUI:
    def __init__(self, pref_dict: dict) -> None:
        # Back end Initialization
        self.exit_code = 0
        self.data_format = pref_dict['data_format'] if 'data_format' in pref_dict else []
        self.header = pref_dict['header']
        self.save_name = pref_dict['file_name'] if pref_dict['file_name'] else 'test_file'
        self.extension = pref_dict['file_ext'] if pref_dict['file_ext'] else 'csv'
        self.main_ui_file = pref_dict['main_ui'] if pref_dict['main_ui'] else 'gui/cugs_mainwindow.ui'
        self.plot_engine = pref_dict['plot_engine']
        self.to_plot_y = pref_dict['use_plot']['y']
        self.to_plot_x = pref_dict['use_plot']['x']
        self.is_save = (pref_dict['is_save'].lower() == 'true')
        self.map_engine = pref_dict['map_engine']
        self.state_key = pref_dict['state_key']
        self.state_id_list = [str(e) for e in pref_dict['state_id']]
        self.state_name_list_upcoming = pref_dict['state_name']
        self.state_name_list_previous = []

        __len_name_state = len(self.state_name_list_upcoming)
        __len_id_state = len(self.state_id_list)

        # State List Initialization
        if __len_id_state > __len_name_state:
            self.state_name_list_upcoming = self.state_id_list
        elif __len_id_state < __len_name_state:
            self.state_name_list_upcoming = self.state_name_list_upcoming[:__len_id_state]

        # Plot_X Broadcasting
        if isinstance(self.to_plot_x, str):
            self.to_plot_x = [self.to_plot_x] * len(self.to_plot_y)
        else:
            if 0 < len(self.to_plot_x) < len(self.to_plot_y):
                self.to_plot_x += [self.to_plot_x[-1]] * (len(self.to_plot_y) - len(self.to_plot_x))

        # Logger Initialization
        self.logger = Log(target='GUI_STACK')

        # Choose Map Engine
        if 'earth' in self.map_engine:
            self.map_engine = 'earth'
        elif self.map_engine:
            self.map_engine = 'included'

        # Create header list
        if isinstance(self.header, str):
            self.header = [self.header]

        # Objects Initialization
        self.ui_main = guilib.GuiLoader(self.main_ui_file).ui
        self.ui_csv = guilib.GuiLoader('gui/cugs_csv_liveview.ui').ui
        self.ui_pref = guilib.GuiLoader('gui/cugs_preferences.ui').ui
        self.parser = ilib.Parser(self.data_format, header=self.header)
        self.directory = ilib.LoadDirectory(__file__, self.save_name, self.extension)
        self.com = ilib.ComPort()
        self.mpl_widgets = [
            self.ui_main.mpl_c1,
            self.ui_main.mpl_c2,
            self.ui_main.mpl_c3,
            self.ui_main.mpl_c4,
            self.ui_main.mpl_c5,
            self.ui_main.mpl_c6,
            self.ui_main.mpl_c7,
            self.ui_main.mpl_c8,
            self.ui_main.mpl_c9
        ]
        self.mpl_title = [
            self.ui_main.lb_main1,
            self.ui_main.lb_main2,
            self.ui_main.lb_sub1,
            self.ui_main.lb_sub2,
            self.ui_main.lb_sub2,
            self.ui_main.lb_sub3,
            self.ui_main.lb_sub4,
            self.ui_main.lb_sub5,
            self.ui_main.lb_sub6,
            self.ui_main.lb_sub7,
        ]
        if self.plot_engine == 'qchart':
            __plot_engine = ilib.QChartData
        elif self.plot_engine == 'pyqtgraph':
            __plot_engine = ilib.PyQtGraphData
        else:
            __plot_engine = None
        if __plot_engine is not None:
            self.mpl_charts = [
                __plot_engine(mpl_w, line_type=['line']) for mpl_w in self.mpl_widgets
            ]

            self.plot_list = [
                [c, x, y]
                for c, x, y in zip(self.mpl_charts,
                                   self.to_plot_x[:len(self.mpl_charts)],
                                   self.to_plot_y[:len(self.mpl_charts)])
            ]
        else:
            self.mpl_charts = []
            self.plot_list = []

        self.table_main = ilib.QTableData(self.ui_main.table_kv_payload)
        self.table_csv = ilib.QTableData(self.ui_csv.table_csv)

        # Variables Initialization
        self.com_baudrate = 0
        self.com_portname = ''
        self.timer_thread = None
        self.serial_logger = None
        self.serial_connected = False
        self.serial_thread = None
        self.serial_plain_text = ''
        self.serial_parsed_dict = dict()
        self.pause_data = False
        self.bool_write_csv = False
        self.bool_write_kml = False
        self.dict_data_array = self.parser.createBlankDataDict()

        # Front end Initialization
        self.setupUi()
        self.connectButons()
        self.updateButtonsLogic()
        self.setSerialDropDown()

        # Other
        pass

    def setupUi(self) -> None:
        # Text
        self.ui_main.setWindowTitle("CU Ground Station V1")
        self.ui_main.combo_serial.clear()
        self.ui_main.text_serial_mon.clear()
        self.ui_main.text_serial_info.clear()
        self.ui_main.text_sys_log.clear()

        # Table
        self.ui_main.table_kv_payload.setRowCount(len(self.data_format))
        for r, k in enumerate(self.data_format):
            self.ui_main.table_kv_payload.setItem(r, 0, QTableWidgetItem(k))

        # Charts
        if self.plot_list:
            for mpl_t, c_name in zip(self.mpl_title, self.to_plot_y):
                mpl_t.setText(c_name)

        return

    def start(self) -> None:
        self.ui_main.show()
        return

    def stop(self) -> int:
        self.serialDisconnect()
        return self.exit_code

    def connectButons(self) -> None:
        self.ui_main.btn_serial_connect.clicked.connect(self.serialConnect)
        self.ui_main.btn_serial_disconnect.clicked.connect(self.serialDisconnect)
        self.ui_main.btn_serial_refresh.clicked.connect(self.listRefreshSerial)

        self.ui_main.cb_write_log.clicked.connect(self.updateButtonsLogic)
        self.ui_main.cb_write_kml.clicked.connect(self.updateButtonsLogic)

        self.ui_main.btn_start_pause_data.clicked.connect(self.updateButtonsLogic)
        self.ui_main.btn_csv_live.clicked.connect(self.windowStartCsvLiveView)

        self.ui_main.btn_serial_mon_clear.clicked.connect(lambda: self.ui_main.text_serial_mon.clear())

        self.ui_main.btn_chart_pop.clicked.connect(self.popPlot)
        self.ui_main.btn_chart_clear.clicked.connect(self.clearPlot)

        self.ui_csv.btn_clear.clicked.connect(lambda: self.table_csv.clear())
        self.ui_csv.btn_pop.clicked.connect(lambda: self.table_csv.pop())

        self.ui_main.actionPreferences.triggered.connect(self.windowStartPreferences)
        return

    def setSerialDropDown(self) -> None:
        self.ui_main.combo_serial.clear()
        self.com.refreshPortList()
        self.ui_main.combo_serial.addItems(self.com.port_dict)
        self.ui_main.combo_serial.addItem('[Simulation Mode]')
        return

    def setupThreadSerial(self) -> None:
        self.serial_thread = ilib.ThreadSerial(serial_logger=self.serial_logger)
        self.serial_thread.msg_carrier.connect(self.updateBackEnds)
        return

    def setupThreadTimer(self) -> None:
        return

    def listRefreshSerial(self) -> None:
        self.setSerialDropDown()
        return

    def serialConnect(self) -> None:
        self.com_baudrate = int(self.ui_main.combo_baud.currentText())
        self.com_portname = self.ui_main.combo_serial.currentText()
        if self.com_portname != '[Simulation Mode]':
            if self.com.connect(self.com_portname, self.com_baudrate):
                self.ui_main.tabWidget_Cmd.setCurrentWidget(self.ui_main.tab_data)
                self.serial_connected = True
                self.serial_logger = ilib.LogSerial(self.com.device, header=self.header)
                self.setupThreadSerial()
                self.serial_thread.start()
        else:
            self.ui_main.tabWidget_Cmd.setCurrentWidget(self.ui_main.tab_data)
            self.serial_logger = ilib.LogSimulation(self.data_format, header=self.header, frequency=5)
            self.setupThreadSerial()
            self.serial_thread.start()
        return

    def serialDisconnect(self) -> None:
        if self.com_portname == '[Simulation Mode]':
            self.serial_thread.stop()
        else:
            try:
                if self.serial_connected:
                    self.serial_thread.stop()
                if self.com.disconnect():
                    self.serial_connected = False
            except Exception:
                return
        return

    def startMission(self) -> None:
        return

    def windowStartCsvLiveView(self) -> None:
        """
        Open CSV Table Live View Table

        :return:
        """
        self.ui_csv.setWindowTitle("CU Ground Station V1 - CSV Tabular Liveview")
        self.ui_csv.show()
        return

    def windowStartPreferences(self) -> None:
        """
        Open Preferences Settings Window

        :return:
        """
        # self.ui_main.setEnabled(False)
        self.ui_pref.setWindowTitle("CU Ground Station V1 - Preferences")
        self.ui_pref.show()

    def updateButtonsLogic(self) -> None:
        self.pause_data = self.ui_main.btn_start_pause_data.isChecked()
        self.bool_write_csv = self.ui_main.cb_write_log.isChecked()
        self.bool_write_kml = self.ui_main.cb_write_kml.isChecked()
        return

    def updateStateBar(self) -> str:
        # Process List
        __curr_state_id = self.serial_parsed_dict[self.state_key]
        if __curr_state_id not in self.state_id_list:
            return ''

        __curr_state_idx = self.state_id_list.index(__curr_state_id)
        __curr_state = self.state_name_list_upcoming[__curr_state_idx]

        self.state_name_list_upcoming.pop(__curr_state_idx)
        self.state_id_list.pop(__curr_state_idx)

        self.state_name_list_previous.append(__curr_state)

        # Update front-end
        # Insert Remaining Scripts Here
        return __curr_state

    def updatePlot(self) -> None:
        __to_plot_data = []
        __max_plot = int(self.ui_main.combo_max_plot.currentText())
        for __chart, __key_x, __key_y in self.plot_list:
            if __key_y not in self.serial_parsed_dict:
                continue
            if __key_x not in self.serial_parsed_dict:
                continue
            if type(self.serial_parsed_dict[__key_y]) not in [int, float]:
                continue
            if type(self.serial_parsed_dict[__key_x]) not in [int, float]:
                continue
            __data_y = self.serial_parsed_dict[__key_y]
            __chart.append(float(self.serial_parsed_dict[__key_x]), __data_y, max_count=__max_plot)
            __chart.setTitle(__data_y, __key_y)
        return

    def clearPlot(self):
        for __chart, _, _ in self.plot_list:
            __chart.clear()
        return

    def popPlot(self):
        for __chart, _, _ in self.plot_list:
            __chart.pop()
        return

    def updateBackEnds(self, serial_text_in) -> None:
        if not self.pause_data:
            # Raw Data Processing
            self.serial_plain_text = serial_text_in
            self.serial_parsed_dict = self.parser.parseData(serial_text_in)

            # Append data (large dict, not recommended) if you want to use these data somewhere else.
            # self.parser.append(self.dict_data_array, self.serial_parsed_dict)

            # Create Coordinate data object
            try:
                __coord = ilib.Coordinate(
                    latitude=self.serial_parsed_dict['gps_lat'],
                    longitude=self.serial_parsed_dict['gps_lon'],
                    altitude=self.serial_parsed_dict['bar_alt']
                )
            except KeyError:
                __coord = ilib.Coordinate(
                    latitude=None,
                    longitude=None,
                    altitude=None
                )

            # Serial Monitor
            self.ui_main.text_serial_mon.appendPlainText(self.serial_plain_text)
            self.ui_main.text_serial_mon.moveCursor(QTextCursor.End)

            # Exit Code
            if not self.exit_code % 200:
                self.ui_main.text_serial_mon.clear()
            self.ui_main.lb_exit_id.setText(str(self.exit_code))

            # File Appending
            if self.is_save and self.bool_write_csv:
                self.directory.appendDelimitedFile(self.directory.dictToList(self.serial_parsed_dict, self.data_format),
                                                   self.serial_plain_text)

            # Map plotting
            if self.bool_write_kml:
                if self.map_engine == 'earth':
                    self.directory.appendEarthCoord(__coord)

            # Key-Value Table
            self.table_main.replaceVector(self.serial_parsed_dict)

            # CSV Liveview Table
            if not self.ui_csv.isHidden():
                self.table_csv.appendTable(self.serial_parsed_dict)

            # Update plot data
            if self.plot_list:
                self.updatePlot()
                pass

            # Update Exit code
            self.exit_code += 1
        return


def run_prog(pref_file_name: str = 'cugs_preferences.json'):
    log = Log(target='GUI_PROG')
    log.info('Start of Program')
    prog_preferences = ilib.PreferencesData('lib/' + pref_file_name).getPreferences()
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    prog = ProgFullStackGUI(prog_preferences)

    prog.start()
    try:
        app.exec()
    except KeyboardInterrupt:
        pass

    prog.stop()
    log.info('Program exited with code ' + str(prog.exit_code))

    return prog.exit_code


if __name__ == '__main__':
    run_prog()
