import sys
import lib as ilib
import gui as guilib
import numpy as np
from lib import Log
from typing import Union as _Union
from PySide6.QtWidgets import QApplication, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor


class ProgFullStackGUI:
    def __init__(self, tuple_data: _Union[list, tuple, set, dict], /, *,
                 header=None, save_name=None, ext=None, use_np: bool = False) -> None:
        # Back end Initialization
        self.exit_code = 0
        self.use_np = use_np
        self.data_format = tuple_data
        self.header = header if header else 'SPARK2'
        self.save_name = save_name if save_name else 'test_file' 
        self.extension = ext if ext else 'csv'
        self.logger = Log(target='GUI_STACK')

        # Objects Initialization
        self.ui_main = guilib.GuiLoader('gui/cugs_mainwindow.ui').ui
        self.parser = ilib.Parser(self.data_format, header=self.header)
        self.directory = ilib.LoadDirectory(__file__, self.save_name, self.extension)
        self.com = ilib.ComPort()
        self.mpl_widgets = [
            ilib.PyQtPlot(e) for e in [
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
        ]

        # Variables Initialization
        self.com_baudrate = 0
        self.com_portname = ''
        self.timer_thread = None
        self.serial_logger = None
        self.serial_connected = False
        self.serial_thread = None
        self.serial_plain_text = ''
        self.serial_parsed_text = dict()
        self.start_mission_stat = False
        self.pause_data = False
        self.dict_data_array = self.parser.createBlankDataDict()

        # Front end Initialization
        self.setupUi()
        self.connectButons()
        self.updateButtonsLogic()
        self.setSerialDropDown()

        # Other
        self.testUpdatePlot()

    def setupUi(self) -> None:
        self.ui_main.setWindowTitle("CU Ground Station V1")
        self.ui_main.combo_serial.clear()
        self.ui_main.text_serial_mon.clear()
        self.ui_main.text_serial_info.clear()
        self.ui_main.text_sys_log.clear()

        self.ui_main.table_kv_payload.setRowCount(len(self.data_format))
        for r, k in enumerate(self.data_format):
            self.ui_main.table_kv_payload.setItem(r, 0, QTableWidgetItem(k))

        return

    def start(self) -> None:
        self.ui_main.show()
        return

    def connectButons(self) -> None:
        self.ui_main.btn_serial_connect.clicked.connect(self.serialConnect)
        self.ui_main.btn_serial_disconnect.clicked.connect(self.serialDisconnect)
        self.ui_main.btn_serial_refresh.clicked.connect(self.listRefreshSerial)
        self.ui_main.btn_start_mission.clicked.connect(self.updateButtonsLogic)
        self.ui_main.btn_start_pause_data.clicked.connect(self.updateButtonsLogic)

        return

    def updateButtonsLogic(self) -> None:
        self.start_mission_stat = self.ui_main.btn_start_mission.isChecked()
        self.pause_data = self.ui_main.btn_start_pause_data.isChecked()
        return

    def setSerialDropDown(self) -> None:
        self.ui_main.combo_serial.clear()
        self.com.refreshPortList()
        self.ui_main.combo_serial.addItems(self.com.port_dict)
        return

    def updateBackEnds(self, serial_text_in) -> None:
        # Raw Data Processing
        self.serial_plain_text = serial_text_in
        self.serial_parsed_text = self.parser.parseData(serial_text_in)
        self.parser.append(self.dict_data_array, self.serial_parsed_text)
        try:
            __coord = ilib.Coordinate(
                latitude=self.serial_parsed_text['gps_lat'],
                longitude=self.serial_parsed_text['gps_lon'],
                altitude=self.serial_parsed_text['bar_alt']
            )
        except KeyError:
            __coord = ilib.Coordinate(
                latitude=None,
                longitude=None,
                altitude=None
            )
            self.logger.warn('GPS Latitude, GPS Longitude, Barometric Altitude are not valid! '
                             'Using Coordinate(0, 0, 0) instead.')

        # Serial Monitor
        self.ui_main.text_serial_mon.appendPlainText(self.serial_plain_text)
        self.ui_main.text_serial_mon.moveCursor(QTextCursor.End)

        # Key-Value Table
        self.ui_main.table_kv_payload.setRowCount(len(self.serial_parsed_text))
        for r, (k, v) in enumerate(self.serial_parsed_text.items()):
            self.ui_main.table_kv_payload.setItem(r, 0, QTableWidgetItem(k))
            self.ui_main.table_kv_payload.setItem(r, 1, QTableWidgetItem(str(v)))

        # File Appending
        self.directory.appendEarthCoord(__coord)
        self.directory.appendDelimitedFile(self.directory.dictToList(self.serial_parsed_text, self.data_format),
                                           self.serial_plain_text)

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
        if self.com.connect(self.com_portname, self.com_baudrate):
            self.ui_main.tabWidget_Cmd.setCurrentWidget(self.ui_main.tab_data)
            self.serial_connected = True
            self.serial_logger = ilib.LogSerial(self.com.device, header=self.header)
            self.setupThreadSerial()
            self.serial_thread.start()
        return

    def serialDisconnect(self) -> None:
        if self.com.disconnect():
            self.serial_connected = False
        return

    def startMission(self) -> None:
        return

    def testUpdatePlot(self) -> None:
        for c in self.mpl_widgets:
            c.plot(1, 2)
        return


def run_prog(pref_file_name: str = 'cugs_preferences.json'):
    log = Log(target='GUI_PROG')
    log.info('Start of Program')
    print()
    prog_preferences = ilib.PreferencesData('lib/' + pref_file_name).getPreferences()
    data_format = prog_preferences['data_format']
    leading_header = prog_preferences['header']
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)

    prog = ProgFullStackGUI(data_format, header=leading_header, use_np=True)
    prog.start()

    app.exec()
    prog.com.disconnect()
    print()
    log.info('Program exited with code ' + str(prog.exit_code))

    return prog.exit_code


if __name__ == '__main__':
    run_prog()
