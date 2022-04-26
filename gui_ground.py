import sys
import data_handler as ilib
import gui as guilib
import numpy as np
from typing import Union as _Union
from PySide6.QtWidgets import QApplication


class ProgFullStackGUI:
    def __init__(self, tuple_data: _Union[list, tuple, set, dict], /, *,
                 header=None, save_name=None, ext=None, use_np: bool = False) -> None:
        # Back end Init
        self.exit_code = 0
        self.use_np = use_np
        self.data_format = tuple_data
        self.header = header if header else 'SPARK2'
        self.save_name = save_name if save_name else 'test_file'
        self.extension = ext if ext else 'csv'
        self.parser = ilib.Parser(self.data_format, header=self.header)
        self.directory = ilib.LoadDirectory(__file__, self.save_name, self.extension)
        self.com = ilib.ComPort()
        self.com_baudrate = 0
        self.com_portname = ''
        self.serial_logger = None
        self.start_mission_stat = False
        self.pause_data = False
        self.dict_data_array = dict()
        _t = np.array([])

        self.func_list = [
            # ilib.wrapper(print, [], {}),
            ilib.wrapper(ilib.printStyled, fg='red', bg='white', style='bold'),
            # ilib.wrapper(self.backgroundTasks)
        ]

        # Front end Init
        self.ui_main = guilib.GuiLoader('gui/cugs_mainwindow.ui').ui
        self.connectButons()
        self.updateButtonsLogic()
        self.setSerialDropDown()

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

        self.testUpdatePlot()

    def start(self):
        self.ui_main.show()
        return

    def connectButons(self) -> None:
        self.ui_main.btn_serial_connect.clicked.connect(self.serialConnect)
        self.ui_main.btn_serial_disconnect.clicked.connect(self.com.disconnect)
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
        return

    def startMission(self) -> None:
        return

    def testUpdatePlot(self):
        self.c1 = ilib.PyQtPlot(self.ui_main.mpl_c1)
        self.c1.plot(1, 2)
        return


def run_prog():
    print('[ GUI_PROG ] ' + 'Start of Program')
    print()
    prog_preferences = ilib.PreferencesData('data_handler/cugs_preferences.json').getPreferences()
    data_format = prog_preferences['data_format']
    leading_header = prog_preferences['header']
    app = QApplication(sys.argv)

    prog = ProgFullStackGUI(data_format, header=leading_header, use_np=True)
    prog.start()

    app.exec()
    prog.com.disconnect()
    print()
    print('[ GUI_PROG ] ' + 'Program exited with code ' + str(prog.exit_code))

    return prog.exit_code


if __name__ == '__main__':
    run_prog()
