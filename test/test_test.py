import sys
from PySide6.QtWidgets import QApplication
from lib import lib_preferences_reader as lpref
from lib import lib_parse_data as lparse
from lib import lib_file_class as lfile
from lib import lib_qchart as lchart
from lib import lib_serial_tools as lserial
from lib.lib_gis import *
from gui.gui_class import *


if __name__ == '__main__':
    print('Start of PROG')
    list_data_format = lpref.PreferencesData('lib/cugs_preferences.json')
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
