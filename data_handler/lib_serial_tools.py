import serial as _serial
import serial.tools.list_ports as _serial_port
from typing import Union as _Union


class ComPort:
    def __init__(self) -> None:
        """
        Serial Port Manipulation Class
        """
        self.port_dict = self.listPorts()
        self.port_list = list()
        self.dir = str()
        self.name = str()
        self.port = str()
        self.port_port = None
        self.device = None

    def listPorts(self) -> dict:
        """
        List all ports available

        :return: Tuple of port directory and port name
        """
        port_name = dict()
        self.port_port = _serial_port.comports()
        for port_iter in self.port_port:
            self.name = str(port_iter.device) + \
                        ' (' + str(port_iter.manufacturer) + \
                        ' ' + str(port_iter.product) + ')'
            port_name[self.name] = port_iter.device
        return port_name

    def refreshPortList(self) -> dict:
        """
        Refreshes port list and returns it.

        :return:
        """
        self.port_dict = self.listPorts()
        self.port_list = sorted(self.port_dict.items())
        return self.port_dict

    def connect(self, selected_name, baud: _Union[int, str]) -> bool:
        """
        Connect serial port

        :param selected_name:
        :param baud:
        :return:
        """
        if selected_name:
            self.port = self.port_dict[selected_name]
            try:
                self.device = _serial.Serial(self.port, baudrate=int(baud), timeout=60)
                print('[LOG_SERIAL] ' + 'Device ' + self.port + ' is successfully connected!')
                return True
            except Exception:
                print('[LOG_SERIAL] ' + 'Unexpected Error. Can\'t connect to port or the port is already connected!')
                print('[LOG_SERIAL] ' + 'PORT ID: ' + self.port)
                return False
        else:
            print('[LOG_SERIAL] ' + 'There is no serial port selected. Select the serial port from the list.')
            return False

    def printPort(self) -> None:
        for i, (k, v) in enumerate(self.port_list, start=1):
            print('-> {:3d}: {} ({})'.format(i, k, v))
        return

    def isConnected(self) -> bool:
        """
        Check if the serial device is connected.

        :return:
        """
        if self.device.isOpen():
            return True
        else:
            return False

    def disconnect(self) -> bool:
        """
        Disconnect serial port

        :return:
        """
        try:
            if self.device.isOpen():
                self.device.close()
                del self.device
                print('[LOG_SERIAL] ' + self.port + ' has been successfully closed!')
            else:
                print('[LOG_SERIAL] ' + self.port + ' has already been disconnected!')
            return True
        except AttributeError:
            print('[LOG_SERIAL] ' + 'The port has not been initialized.')
            return False


class LogSerial:
    def __init__(self, device: _serial.serialwin32.Serial, /, *, header='PSG') -> None:
        """
        Serial Logger object class

        :param device:
        :param header:
        """
        self.device = device
        self.header = header
        self.raw = ''
        self.payload = ''
        self.buffer = ''
        self._is_updated = False
        self._find1 = 0
        self._find2 = 0

    def readAll(self, *func) -> None:
        """
        Read all in forever loop

        :return:
        """
        result = None
        print('_' * 20 + 'LOG_SERIAL' + '_' * 20)
        try:
            while result is None:
                try:
                    self.raw += self.__read()
                    self._find1 = self.raw.find(self.header)
                    self._find2 = self.raw.rfind(self.header)

                    if self._find2 > self._find1 >= 0:
                        self.payload = self.raw[self._find1:self._find2]
                        self.raw = self.raw.replace(self.payload, '', 1)
                        self._is_updated = True

                        for f in func:
                            f(self.payload)

                except _serial.serialutil.SerialException:
                    result = ''
        except KeyboardInterrupt:
            pass
        print('_' * 20 + 'END_SERIAL' + '_' * 20)

    def readLine(self) -> str:
        """
        Upcoming

        :return:
        """
        # make a readline function without forever loop
        return ''

    def isUpdated(self) -> bool:
        """
        Returns if payload is updated.

        :return:
        """
        return self._is_updated

    def getPayload(self) -> str:
        """
        Pull latest data from payload.

        :return:
        """
        self._is_updated = False
        return self.payload

    def __read(self) -> str:
        """
        (Private) Read data from serial.

        :return:
        """
        try:
            s = self._pStrip(self.device.read().decode('utf-8')).strip()
        except UnicodeDecodeError:
            s = ''
        return s

    @staticmethod
    def _pStrip(s) -> str:
        return s.replace('\r', '').replace('\n', '')


if __name__ == '__main__':
    pass
