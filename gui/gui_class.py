from PySide6.QtWidgets import QMainWindow as _QMainWindow

class GuiLoader(_QMainWindow):
    def __init__(self, ui_filename: str):
        '''
        Load Qt UI file and generate window

        ====================================

        For .ui file name:

        - Call GuiLoader('...').ui and use .show, .method, .elem

        ====================================

        For .py file name:

        - Call GuiLoader('...') and use .show, .ui.method, .ui.elem

        :param _ui_filename: UI file path or name
        '''
        __extension = ui_filename[ui_filename.rfind('.') + 1:]

        if __extension == 'ui':
            import sys
            from PySide6.QtUiTools import QUiLoader
            from PySide6.QtCore import QFile, QIODevice

            super(GuiLoader, self).__init__()
            self.__ui_filename = ui_filename
            self.__ui_file = QFile(self.__ui_filename)
            if not self.__ui_file.open(QIODevice.ReadOnly):
                print(f'Cannot open {self.__ui_filename}: {self.__ui_file.errorString()}')
                sys.exit(-1)
            self.__loader = QUiLoader()
            self.ui = self.__loader.load(self.__ui_file)
            self.__ui_file.close()
            if not self.ui:
                print(self.__loader.errorString())
                sys.exit(-1)

        elif __extension == 'py':
            import platform
            from gui import cugs_mainwindow

            _QMainWindow.__init__(self)
            self.ui = cugs_mainwindow.Ui_MainWindow()
            self.ui.setupUi(self)
            self.setWindowTitle('CUGS V1')
            if platform.system() == 'Windows':
                self.ui.tabWidget_Cmd.setDocumentMode(True)
            else:
                self.ui.tabWidget_Cmd.setDocumentMode(False)
            pass


# class GuiPy(_QMainWindow):
#     def __init__(self):
#         import platform
#
#         _QMainWindow.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.setWindowTitle('CUGS V1')
#         if platform.system() == 'Windows':
#             self.ui.tabWidget_Cmd.setDocumentMode(True)
#         else:
#             self.ui.tabWidget_Cmd.setDocumentMode(False)

