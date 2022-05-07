import serial as _serial
import serial.tools.list_ports as _serial_port
from typing import Union as _Union
from lib.lib_log import Log


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
        self.logger = Log(target='LOG_SERIAL')

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
            self.port = self.port_dict[selected_name.strip()]
            try:
                self.device = _serial.Serial(self.port, baudrate=int(baud), timeout=60)
                self.logger.info('Device ' + self.port + ' is successfully connected!')
                self.logger.info('with baud rate=' + str(baud) + '.')
                return True
            except Exception:
                self.logger.exception('Unexpected Error. Can\'t connect to port or the port is already connected!')
                self.logger.critical('PORT ID: ' + self.port)
                return False
        else:
            self.logger.warn('There is no serial port selected. Select the serial port from the list.')
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
            self.logger.debug('The device port {} is opened.'.format(self.port))
            return True
        else:
            self.logger.debug('The device port is closed or not initialized.')
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
                self.logger.info(self.port + ' has been successfully closed!')
            else:
                self.logger.warn(self.port + ' has already been disconnected!')
            return True
        except AttributeError:
            self.logger.critical('The port has not been initialized.')
            return False


class LogSerial:
    def __init__(self, device: _serial.Serial, /, *, header='PSG') -> None:
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
        self.logger = Log()

    def readAll(self, *func) -> None:
        """
        Read all in forever loop

        :return:
        """
        result = True
        try:
            while result:
                try:
                    self.raw += self.__read()
                    self._find1 = self.raw.find(self.header)
                    self._find2 = self.raw.rfind(self.header)

                    if self._find2 > self._find1 >= 0:
                        self.payload = self.raw[self._find1:self._find2]
                        self.raw = self.raw.replace(self.payload, '', 1)
                        self._is_updated = True

                        if func:
                            for __f, __args, __kwargs in func:
                                __f(self.payload, *__args, **__kwargs)

                except _serial.serialutil.SerialException:
                    self.logger.exception('Unknown Serial Exception')
                    result = False
                except TypeError:
                    self.logger.exception('Serial port disconnected.')
                    result = False
        except KeyboardInterrupt:
            pass

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
        __stat_device = None
        try:
            __stat_device = self.device.isOpen()
        except AttributeError or TypeError:
            pass
        if __stat_device:
            __sr_in = self.device.read()
            if isinstance(__sr_in, bytes):
                __s = self.__pStrip(__sr_in.decode('utf-8', errors='replace'))
            else:
                __s = ''
        else:
            __s = ''
        return __s

    @staticmethod
    def __pStrip(s) -> str:
        return s.replace('\r', '').replace('\n', '').strip()


if __name__ == '__main__':
    pass
