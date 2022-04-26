import time
import data_handler as _ilib
from PySide6.QtCore import QThread, Signal

class ThreadSerial(QThread):
    msg_carrier = Signal(object)

    def __init__(self, *args, parent=None, serial_logger, **kwargs) -> None:
        super(ThreadSerial, self).__init__(parent)
        self.serial_logger = serial_logger
        self.args = args
        self.kwargs = kwargs
        self._isRunning = True

    def __del__(self) -> None:
        try:
            self.wait()
        except RuntimeError:
            pass
        return

    def run(self) -> None:
        self.serial_logger.readAll(_ilib.wrapper(self.update_msg))
        return

    def stop(self) -> None:
        self._isRunning = False
        self.terminate()
        return

    def update_msg(self, str_out) -> None:
        self.msg_carrier.emit(str_out)
        return
