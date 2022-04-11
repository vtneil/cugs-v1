import sys
from PySide6.QtWidgets import QApplication
from data_handler import lib_preferences_reader as lpref
from data_handler import lib_parse_data as lparse
from data_handler import lib_file_class as lfile
from data_handler import lib_pyqtchart as lchart
from data_handler import lib_serial_tools as lserial
from data_handler.lib_gis import *
from gui.gui_class import *


if __name__ == '__main__':
    print('Start of PROG')
    list_data_format = lpref.PreferencesData('data_handler/cugs_preferences.json')
    # list_data_format.writePreferences('crab')
    # app = QApplication(sys.argv)
    # ui_home = gc.LoadUi('gui/hw_ref.ui')
    # ui_window = ui_home.getWindow()
    # ui_window.show()
    # sys.exit(app.exec())
    dict_coord = Coordinate(latitude= 13.12345,longitude=100.243,altitude= 12.03)
    dict_coord.latitude = 1
    data_sample1 = '1,2,3,4,5,6,7'
    data_sample2 = [7, 6, 5, 4, 3, 2, 1]

    data_parser = lparse.Parser(list_data_format.getPreferences(), header='SP2')
    print(list_data_format.getPreferences())
    # directory_object = lfile.LoadDirectory('test_30_03', 'csv', dir_filename=__file__)
    # print(directory_object.getRootPath())
    # directory_object.appendDelimitedFile(data_sample1)
    # directory_object.appendDelimitedFile(data_sample2)
    # directory_object.appendEarthCoord(dict_coord)
    # directory_object.appendEarthCoord(dict_coord)
    # directory_object.appendEarthCoord(dict_coord)
