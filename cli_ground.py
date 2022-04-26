import data_handler as ilib
import numpy as np
from typing import Union as _Union


class ProgFullStackCLI:
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
        self.func_list = [
            # ilib.wrapper(print, [], {}),
            ilib.wrapper(ilib.printStyled, fg='red', bg='white', style='bold'),
            ilib.wrapper(self.backgroundTasks)
        ]

        self.to_plot = []
        self.dict_data_array = dict()

    def start(self) -> None:
        self.getPortBaudFromUser()
        self.com.connect(self.com_portname, self.com_baudrate)
        self.serial_logger = ilib.LogSerial(self.com.device, header=self.header)
        self.backEnd()
        return

    def backEnd(self) -> None:
        self.serial_logger.readAll(*self.func_list)
        return

    def backgroundTasks(self, _get_data_from_serial) -> None:
        __data_raw = _get_data_from_serial
        __data_dict = self.parser.parseData(__data_raw)
        print(', '.join(['{}: {}'.format(ilib.strStyled(k, style='bold', end=''), v) for k, v in __data_dict.items()]))
        # func keep data to total dict with numpy or list within dict
        print('\n')
        __coord = ilib.Coordinate(
            latitude=__data_dict['gps_lat'],
            longitude=__data_dict['gps_lon'],
            altitude=__data_dict['bar_alt']
        )
        self.directory.appendEarthCoord(__coord)
        self.directory.appendDelimitedFile(self.directory.dictToList(__data_dict, self.data_format), __data_raw)

        if self.use_np:
            for k, v in __data_dict.items():
                if k not in self.dict_data_array:
                    self.dict_data_array[k] = np.array([])
                self.dict_data_array[k] = np.append(self.dict_data_array[k], v)
        else:
            for k, v in __data_dict.items():
                if k not in self.dict_data_array:
                    self.dict_data_array[k] = []
                self.dict_data_array[k].append(v)

        return

    def frontEnd(self) -> None:
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
        print('[ CLI_PROG ] ' + 'Type \'refresh\' to refresh port')
        try:
            __user_input = input('[ CLI_PROG ] ' + 'Input ID from listed port (Leave blank if first from list): ') \
                .strip()
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
                __user_input = input('[ CLI_PROG ] ' + 'Input Baudrate (Leave blank if 115200): ').strip()
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
            ilib.scrollConsole()
            print('[ CLI_PROG ] ' + 'Set {} as ComPort with baudrate={}'.format(self.com_portname, self.com_baudrate))
            print('=' * 50)
            print()
        return

    def stop(self):
        return


def run_prog():
    print('[ CLI_PROG ] ' + 'Start of Program')
    print()
    prog_preferences = ilib.PreferencesData('data_handler/cugs_preferences.json').getPreferences()
    data_format = prog_preferences['data_format']
    leading_header = prog_preferences['header']
    prog = ProgFullStackCLI(data_format, header=leading_header, use_np=True)
    prog.start()

    try:
        prog.stop()
        print('[ CLI_PROG ] ' + 'Threads stopped successfully.')
    except AttributeError:
        print('[ CLI_PROG ] ' + 'Tried to stop threads but the threads does not exist.')
    prog.com.disconnect()
    print()
    print('[ CLI_PROG ] ' + 'Program exited with code ' + str(prog.exit_code))

    return prog.exit_code


if __name__ == '__main__':
    run_prog()
