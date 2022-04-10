import sys
import os
import data_handler as ilib
from typing import Union as _Union


class ProgFullStackCLI:
    def __init__(self, tuple_data: _Union[list, tuple, set, dict], /, *,
                 header=None, save_name=None, ext=None) -> None:
        # Back end Init
        self.exit_code = 0
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
        self.func_list = [print, self.backEnd]

    def start(self) -> None:
        self.getPortBaudFromUser()
        self.com.connect(self.com_portname, self.com_baudrate)
        self.serial_logger = ilib.LogSerial(self.com.device, header=self.header)
        self.serial_logger.readAll(*self.func_list)
        return

    def backEnd(self, _get_data_from_serial) -> None:
        __data_dict = self.parser.parseData(_get_data_from_serial)
        for k, v in __data_dict.items():
            print('{}: {}'.format(k, v), end=', ')
        print('\n')
        __coord = ilib.Coordinate(
            latitude=__data_dict['gps_lat'],
            longitude=__data_dict['gps_lon'],
            altitude=__data_dict['bar_alt']
        )
        self.directory.appendEarthCoord(__coord)
        self.directory.appendDelimitedFile(self.directory.dictToList(__data_dict, self.data_format))
        return

    def listRefreshSerial(self) -> None:
        self.com.refreshPortList()
        self.com.printPort()
        return

    def getPortBaudFromUser(self) -> None:
        __port_name = ''
        __baudrate = 0
        __goto_baud = True
        __successful = True
        print('-' * 50)
        self.listRefreshSerial()
        print('-' * 50)
        print('Type \'refresh\' to refresh port')
        try:
            __user_input = input('Input ID from listed port (Leave blank if first from list): ').strip()
        except KeyboardInterrupt:
            return
        if not __user_input:
            __user_input = '1'
        if __user_input == 'refresh' or not __user_input.isdigit():
            __goto_baud = False
            __successful = False
            self.getPortBaudFromUser()
        else:
            __idx = int(__user_input) - 1
            if 0 <= __idx < len(self.com.port_list):
                __port_name, _ = self.com.port_list[__idx]
                print('-' * 50)
            else:
                __goto_baud = False
                __successful = False
                self.getPortBaudFromUser()
        if __goto_baud:
            try:
                __user_input = input('Input Baudrate (Leave blank if 115200): ').strip()
            except KeyboardInterrupt:
                return
            if __user_input:
                if __user_input in ['4800', '9600', '19200', '38400', '57600', '76800', '115200'] \
                        and __user_input.isdigit():
                    __baudrate = int(__user_input)
                    print('-' * 50)
                else:
                    __successful = False
                    self.getPortBaudFromUser()
            else:
                __baudrate = 115200
                print('-' * 50)
        if __successful:
            self.com_portname = __port_name
            self.com_baudrate = __baudrate
            self.clearConsole()
            print('Set {} as ComPort with baudrate={}'.format(self.com_portname, self.com_baudrate))
            print('=' * 50)
            print()
        return

    @staticmethod
    def clearConsole() -> None:
        print('\n' * 150)
        return


if __name__ == '__main__':
    print('[ CLI_PROG ] ' + 'Start of Program')
    print()
    prog_preferences = ilib.PreferencesData('data_handler/data_format.txt').getPreferences()
    data_format = prog_preferences['data_format']
    prog = ProgFullStackCLI(data_format)
    prog.start()

    prog.com.disconnect()
    print()
    print('[ CLI_PROG ] ' + 'Program exited with code ' + str(prog.exit_code))
