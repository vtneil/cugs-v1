from PySide6.QtCore import QThread, Signal
from threading import Thread
import time


class PyThreadWorker(Thread):
    def __init__(self, InputClass, interval=500):
        """
        Upcoming features for CLI thread.
        :param InputClass:
        :param interval:
        """
        Thread.__init__(self)

        self.__InputClass = InputClass
        self.__interval = interval / 1000

    def run(self):
        while True:
            time.sleep(self.__interval)


class QThreadWorker(QThread):
    msg_carrier = Signal(object)

    def __init__(self, InputClass, /, *args, parent=None, **kwargs) -> None:
        super(QThreadWorker, self).__init__(parent)
        self.args = args
        self.kwargs = kwargs
        self.cls = InputClass
        self._isRunning = True

    def __del__(self) -> None:
        self.wait()

    def run(self) -> None:
        try:
            self.cls(*self.args, **self.kwargs)
        except TypeError:
            raise TypeError('Missing positional/keyword Arguments')

    def stop(self) -> None:
        self._isRunning = False
        self.terminate()
