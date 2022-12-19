import serial as _serial
import time as _time
import numpy as _np
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
    def __init__(self, device: _serial.Serial, /, *, header) -> None:
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
        self.logger = Log(target='LOG_SERIAL')
        self.read_result = True

    def readPayload(self, *func) -> None:
        """
        Read all in forever loop

        :return:
        """
        try:
            if self.header:
                self.readFromUntil(self.header, *func)
            else:
                self.readLine(*func)
        except Exception:
            pass

    def readFromUntil(self, header, *func):
        while self.read_result:
            try:
                for __header in header:
                    self.raw += self.__read()
                    self._find1 = self.raw.find(__header)
                    self._find2 = self.raw.find(__header, self._find1 + 1)

                if self._find2 > self._find1 >= 0:
                    self.payload = self.raw[self._find1:self._find2]
                    self.raw = self.raw[self._find2:]
                    self._is_updated = True

                    if func:
                        for __f, __args, __kwargs in func:
                            __f(self.payload, *__args, **__kwargs)

            except _serial.serialutil.SerialException:
                self.logger.exception('Unknown Serial Exception')
                break
            except TypeError:
                self.logger.exception('Serial port disconnected.')
                break
            except Exception:
                self.logger.exception('Unknown Other Exceptions')
                break

    def readLine(self, *func):
        while self.read_result:
            try:
                self.payload = self.device.readline().decode('utf-8', errors='replace')
                self.payload = self.payload.replace('\r', '').replace('\n', '')
                self._is_updated = True

                if func:
                    for __f, __args, __kwargs in func:
                        __f(self.payload, *__args, **__kwargs)

            except _serial.serialutil.SerialException:
                self.logger.exception('Unknown Serial Exception')
                break
            except TypeError:
                self.logger.exception('Serial port disconnected.')
                break
            except Exception:
                self.logger.exception('Unknown Other Exceptions')
                break

    def isUpdated(self) -> bool:
        """
        Returns if payload is updated.

        :return:
        """
        return self._is_updated

    def getPayload(self) -> str:
        """
        Pull the latest data from payload.

        :return:
        """
        self._is_updated = False
        return self.payload

    def __read(self) -> str:
        """
        (Private) Read data from serial.

        :return:
        """
        __stat_device = True
        __s = ''
        try:
            __stat_device = self.device.isOpen()
        except Exception:
            __stat_device = False
        if __stat_device:
            try:
                __sr_in = self.device.read()
            except Exception:
                return __s
            if isinstance(__sr_in, bytes):
                __s = self.__pStrip(__sr_in.decode('utf-8', errors='replace'))
        return __s

    @staticmethod
    def __pStrip(s) -> str:
        return s.replace('\r', '').replace('\n', '').strip()


class LogSimulation:
    def __init__(self, data_format, /, *, header, override: list = None, frequency: float = 0.5):
        self.data_format = data_format
        self.data_length = len(self.data_format)
        self.header = header[0]
        self.payload = ''
        self.override = [] if override else override
        self.read_result = True
        self.logger = Log(target='LOG_SIM')
        _np.random.seed(6185293)
        self.logger.info('Simulation Thread Started')
        self.counter = 1
        self.period = 1 / frequency
        return

    def readPayload(self, *func) -> None:
        while self.read_result:
            _time.sleep(self.period)
            self.payload = self.updateSimulation()
            if func:
                for __f, __args, __kwargs in func:
                    __f(self.payload, *__args, **__kwargs)
            self._is_updated = True
        return

    def updateSimulation1(self) -> str:
        __payload = ''
        with open('../data/test_raw_1_20.txt') as f:
            __payload = f.readlines()
            if self.counter >= len(__payload):
                return ''
            self.counter += 1
            return __payload[self.counter].strip()

    def updateSimulation(self) -> str:
        rand_np = _np.random.uniform(13.0, 14.0, self.data_length - 3)
        if self.data_format[0] == 'team_id':
            __payload = self.header + ',00:00:00,'
        else:
            __payload = 'SPARK2,00:00:00,'
        __payload += str(self.counter) + ','
        __payload += ','.join(['{:.6f}'.format(__e) for __e in rand_np])
        self.counter += 1
        return __payload

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


if __name__ == '__main__':
    pass
