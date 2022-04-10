import sys
from typing import Union as _Union
from PySide6.QtWidgets import QApplication
from data_handler import lib_preferences_reader as lpref
from data_handler import lib_parse_data as lparse
from data_handler import lib_file_class as lfile
from data_handler import lib_pyqtchart as lchart
from data_handler import lib_serial_tools as lserial
from data_handler.lib_threading import *
from gui.gui_class import *


class ProgFullStack:
    def __init__(self, tuple_data: _Union[list, tuple, set, dict], /):
        # Back end Init
        self.exit_code = 0
        self.data_format = tuple_data
        # self.parser = lparse.Parser(self.data_format, header='SPARK2')
        self.com = lserial.ComPort()
        self.com_baudrate = 0
        self.com_portname = ''

        # Front end Init
        self.ui_main = GuiLoader('gui/cugs_mainwindow.ui').ui
        self.ui_main.show()

        self.connectButons()
        self.updateButtonsLogic()
        self.setSerialDropDown()

    def connectButons(self) -> None:
        self.ui_main.btn_serial_connect.clicked.connect(self.serialConnect)
        self.ui_main.btn_serial_disconnect.clicked.connect(self.com.disconnect)
        self.ui_main.btn_serial_refresh.clicked.connect(self.setSerialDropDown)

        self.ui_main.btn_start_mission.clicked.connect(self.updateButtonsLogic)
        self.ui_main.btn_start_pause_data.clicked.connect(self.updateButtonsLogic)
        return

    def updateButtonsLogic(self) -> None:
        self.start_mission_stat = self.ui_main.btn_start_mission.isChecked()
        self.pause_data = self.ui_main.btn_start_pause_data.isChecked()

        return

    def setSerialDropDown(self) -> None:
        self.ui_main.combo_serial.clear()
        self.com.port_list = self.com.listPorts()
        self.ui_main.combo_serial.addItems(self.com.port_list)
        return
    
    def setupThreadTimer(self) -> None:
        return

    def serialConnect(self) -> None:
        self.com_baudrate = self.ui_main.combo_baud.currentText()
        self.com_portname = self.ui_main.combo_serial.currentText()
        self.com.connect(self.com_portname, self.com_baudrate)
        return

    def startMission(self) -> None:

        return


if __name__ == '__main__':
    print('[ GUI_PROG ] ' + 'Start of Program')
    print()

    prog_preferences = lpref.PreferencesData('data_handler/data_format.txt').getPreferences()
    # prog_d = lpref.PreferencesData(1)
    # print(str(prog_d))

    app = QApplication(sys.argv)
    prog = ProgFullStack(prog_preferences)

    app.exec()
    prog.com.disconnect()
    print()
    print('[ GUI_PROG ] ' + 'Program exited with code ' + str(prog.exit_code))
