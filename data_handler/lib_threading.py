from PySide6.QtCore import QThread, Signal


class ThreadWorker(QThread):
    msg_carrier = Signal(object)

    def __init__(self, InputClass, /, *args, parent=None, **kwargs) -> None:
        super(ThreadWorker, self).__init__(parent)
        self.args = args
        self.kwargs = kwargs
        self.internal_class = InputClass
        self._isRunning = True

    def __del__(self) -> None:
        self.wait()

    def run(self) -> None:
        try:
            self.internal_class(*self.args, **self.kwargs)
        except TypeError:
            raise TypeError('Missing positional/keyword Arguments')

    def stop(self) -> None:
        self._isRunning = False
        self.terminate()
