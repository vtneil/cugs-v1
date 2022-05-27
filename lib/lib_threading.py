import time
import lib as _ilib
from lib.lib_log import Log
from PySide6.QtCore import QThread, Signal

class ThreadSerial(QThread):
    msg_carrier = Signal(object)

    def __init__(self, *args, parent=None, serial_logger, **kwargs) -> None:
        super(ThreadSerial, self).__init__(parent)
        self.serial_logger = serial_logger
        self.args = args
        self.kwargs = kwargs
        self.logger = Log(target='LOG_THREAD')
        self._isRunning = True

    def __del__(self) -> None:
        try:
            self.wait()
            self.logger.info('Serial thread deleted successfully.')
        except RuntimeError:
            self.logger.exception('Unable to delete the serial thread.')
            pass
        return

    def run(self) -> None:
        self.logger.info('Starting the serial thread.')
        try:
            self.serial_logger.readPayload(_ilib.wrapper(self.update_msg))
        except Exception:
            return
        return

    def stop(self) -> None:
        self.logger.info('Try stopping the serial thread.')
        self._isRunning = False
        self.terminate()
        self.logger.info('Stopped the serial thread.')
        return

    def update_msg(self, str_out) -> None:
        self.logger.debug('Emitted ' + str(str_out))
        self.msg_carrier.emit(str_out)
        return
