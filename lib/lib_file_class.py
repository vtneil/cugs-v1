import os.path as _op
import numpy as _np
import os
from typing import Union as _Union
from lib.lib_log import Log
from lib.lib_gis import Coordinate as _Coordinate
from collections import OrderedDict as _Dict


class LoadDirectory:
    def __init__(self, dir_filename: str, save_name: str, delim_extension: str, /, *,
                 earth_save_name: str = 'gearthcoord_save', device_id: _Union[int, str] = '1',
                 folder_name: str = 'data') -> None:
        """
        A class to create and manage directory and files in directory for
        special use cases in the ground control station.

        :param save_name: File name for delimited file
        :param delim_extension: File extension for delimited file
        :param earth_save_name: File name for Coordinate KML file
        :param dir_filename: Directory path must input '__file__' every time
        :param device_id: Device identification number or test number for files
        :param folder_name" Subfolder name for all data and temporary files to be saved
        """
        self.logger = Log(target='LOG_FILE')
        self.dir_filename = dir_filename
        self.global_path = self.getRootPath()
        self.device_id = str(device_id)
        self.save_name = save_name
        self.pre_save = earth_save_name
        self.extension = delim_extension
        if self.extension[0] == '.':
            self.extension = self.extension[1:]
        self.folder_name = folder_name
        self.name_temp_coord = 'tempcoord' + self.device_id + '.tmp'
        self.name_earth_coord = 'gearthcoord' + self.device_id + '.kml'
        self.name_earth_live = 'gearthlive' + self.device_id + '.kml'
        self.path_csv = ''
        self.path_raw = ''
        self.path_save_coord = ''
        self.path_temp_coord = self.__makeAbsolutePath(self.name_temp_coord)
        self.path_earth_coord = self.__makeAbsolutePath(self.name_earth_coord)
        self.path_earth_live = self.__makeAbsolutePath(self.name_earth_live)

        self.__checkFolder()
        self.__checkPath()
        self.__renewPath()

    def __checkFolder(self) -> None:
        """
        Check if subfolder exists.

        :return:
        """
        self.createFolder(self.folder_name)
        self.logger.debug('Checked folder.')
        return

    def __checkPath(self, data_no: int = 1) -> None:
        """
        Check file name with iteration until the files are unique.

        :param data_no: Number to start file name iteration check
        :return:
        """
        self.__checkFolder()
        self.path_csv = self.__makeAbsolutePath(self.save_name + '_' + self.device_id +
                                                '_' + str(data_no) + '.' + self.extension)
        self.path_raw = self.__makeAbsolutePath(self.save_name + '_raw_' + self.device_id +
                                                '_' + str(data_no) + '.txt')
        self.path_save_coord = self.__makeAbsolutePath(self.pre_save + '_' + self.device_id +
                                                       '_' + str(data_no) + '.kml')
        while _op.isfile(self.path_csv) or _op.isfile(self.path_save_coord):
            data_no += 1
            self.path_csv = self.__makeAbsolutePath(self.save_name + '_' + self.device_id +
                                                    '_' + str(data_no) + '.' + self.extension)
            self.path_raw = self.__makeAbsolutePath(self.save_name + '_raw_' + self.device_id +
                                                    '_' + str(data_no) + '.txt')
            self.path_save_coord = self.__makeAbsolutePath(self.pre_save + '_' + self.device_id +
                                                           '_' + str(data_no) + '.kml')
        self.logger.debug('Checked path.')
        return

    def __makeAbsolutePath(self, filename) -> str:
        """
        Returns full absolute path with folder and file name.

        :param filename: File name
        :return: Path to file
        """
        folder = self.folder_name + '/' + filename
        path = _op.join(self.global_path, folder)
        self.logger.debug('Absolute path created.')
        return str(path)

    def __renewPath(self) -> None:
        """
        Renews path, clears old temporary files and creates a new one.

        :return:
        """
        if _op.isfile(self.path_temp_coord):
            os.remove(self.path_temp_coord)
        if _op.isfile(self.path_earth_coord):
            os.remove(self.path_earth_coord)
        if not _op.isfile(self.path_earth_live):
            self.createEarthLive(filename=self.path_earth_live, coord_filename=self.path_earth_coord)
        self.logger.debug('Path renewed.')
        return

    def appendEarthCoord(self, coords: _Coordinate, /, *,
                         color: _Union[str, tuple] = 'ff00ffff') -> str:
        """
        Append new coordinates to Google Earth KML coordinates file.

        :param coords: Dictionary of coordinates containing keys: latitude, longitude, altitude
        :param color: Color code ARGB in tuple or ABGR in hexadecimal string
        :return: String of Google Earth KML coordinates file
        """
        earth_coord_0 = '<kml xmlns="http://www.opengis.net/kml/2.2" ' \
                        'xmlns:gx="http://www.google.com/kml/ext/2.2">\n' + \
                        '<Folder>\n' + \
                        '\t<name>Log</name>\n' + \
                        '\t<Placemark>\n' + \
                        '\t\t<name>Device Path Plotting</name>\n' + \
                        '\t\t<Style>\n' + \
                        '\t\t\t<LineStyle>\n\t\t\t\t<color>'
        earth_coord_1 = '</color>\n\t\t\t\t<colorMode>normal</colorMode>\n' + \
                        '\t\t\t\t<width>3</width>\n' + \
                        '\t\t\t</LineStyle>\n' + \
                        '\t\t\t<PolyStyle>\n' + \
                        '\t\t\t\t<color>99000000</color>\n' + \
                        '\t\t\t\t<fill>1</fill>\n' + \
                        '\t\t\t</PolyStyle>\n' + \
                        '\t\t</Style>\n' + \
                        '\t\t<LineString>\n' + \
                        '\t\t\t<extrude>1</extrude>\n' + \
                        '\t\t\t<altitudeMode>absolute</altitudeMode>\n' + \
                        '\t\t\t<coordinates>\n'
        earth_coord_2 = '\t\t\t</coordinates>\n' + \
                        '\t\t</LineString>\n' + \
                        '\t</Placemark>\n' + \
                        '</Folder>\n' + \
                        '</kml>'
        __color = ''
        if isinstance(color, tuple) and len(color) == 4:
            for code in reversed(color):
                __color += '{:02x}'.format(code)
        else:
            __color = color
        try:
            __latitude = '{:.6f}'.format(coords.latitude)
        except KeyError:
            raise KeyError('Key error raised! Check for latitude key spelling.')
        try:
            __longitude = '{:.6f}'.format(coords.longitude)
        except KeyError:
            raise KeyError('Key error raised! Check for longitude key spelling.')
        try:
            __altitude = '{:.2f}'.format(coords.altitude)
        except KeyError:
            raise KeyError('Key error raised! Check for altitude key spelling.')

        __coord = ','.join([__longitude, __latitude, __altitude]) + '\n'
        with open(self.path_temp_coord, mode='a+', encoding='utf-8') as f_temp, \
                open(self.path_earth_coord, mode='w', encoding='utf-8') as f_gearth, \
                open(self.path_save_coord, mode='w', encoding='utf-8') as f_save:
            f_temp.writelines(__coord)
            str_coord = [earth_coord_0]
            f_temp.seek(0)
            all_coord = f_temp.readlines()
            str_coord.append(__color)
            str_coord.append(earth_coord_1)
            str_coord.extend(all_coord)
            str_coord.append(earth_coord_2)
            f_gearth.writelines(str_coord)
            f_save.writelines(str_coord)
        self.logger.debug('Earth Coord File appended successfully!')
        return earth_coord_0 + color + earth_coord_1 + '\n'.join(__coord) + earth_coord_2

    def appendDelimitedFile(self, *args: _Union[_np.ndarray, list, str], delimiter: str = ',') -> list:
        """
        Append a data file in a form of delimited string file, e.g., CSV.

        :param raw_data: Raw data, either full string with delimiter or a list of data
        :param delimiter: String delimiter
        :return: Raw data
        """
        __raw_data = []
        __raw_data_str = ''
        for raw_data in args:
            if raw_data:
                if isinstance(raw_data, list):
                    __raw_data.append(delimiter.join([str(dat) for dat in raw_data]))
                elif isinstance(raw_data, _np.ndarray):
                    __raw_data.append(delimiter.join([str(dat) for dat in raw_data]))
                elif isinstance(raw_data, str):
                    __raw_data_str += raw_data.strip()
                else:
                    __raw_data.append(str(raw_data).strip())
        if __raw_data:
            with open(self.path_csv, 'a', encoding='utf-8') as _file:
                __lst_tmp = [''.join([__data, '\n']) for __data in __raw_data]
                _file.writelines(__lst_tmp)
                self.logger.debug('Delimited File appended successfully!')
        if __raw_data_str:
            with open(self.path_raw, 'a', encoding='utf-8') as _file:
                _file.writelines([__raw_data_str, '\n'])
                self.logger.debug('Raw Data File appended successfully!')
        return __raw_data

    def getRootPath(self) -> str:
        """
        Get a root path

        :return: Root path
        """
        __filename = self.dir_filename
        return _op.abspath(_op.dirname(__filename))

    def createEarthLive(self, *, filename: str, coord_filename: str) -> str:
        """
        Create or overwrite Google Earth Live Feed KML file.

        :param filename: Google Earth Live Feed KML File path or name
        :param coord_filename: Google Earth Coordinates KML File path or name
        :return:
        """
        earth_live_pre = '<?xml version="1.0" encoding="UTF-8"?>\n' + \
                         '<kml xmlns="http://www.opengis.net/kml/2.2" ' \
                         'xmlns:gx="http://www.google.com/kml/ext/2.2">\n' + \
                         '\t<NetworkLink>\n' + \
                         '\t\t<Link>\n\t\t\t<href>'
        earth_live_post = '</href>\n\t\t\t<refreshMode>onInterval</refreshMode>\n' + \
                          '\t\t\t<refreshInterval>0.1</refreshInterval>\n' + \
                          '\t\t</Link>\n' + \
                          '\t</NetworkLink>\n' + \
                          '</kml>\n'
        with open(filename, mode='w', encoding='utf-8') as f:
            f.writelines(earth_live_pre)
            f.writelines(coord_filename)
            f.writelines(earth_live_post)

        self.logger.debug('Earth Live File created successfully!')

        return earth_live_pre + coord_filename + earth_live_post

    @staticmethod
    def dictToList(raw_dict: _Union[_Dict, dict], tuple_data: _Union[list, tuple, set, dict]) -> list:
        return [raw_dict[key_avail] if key_avail in raw_dict else '' for key_avail in tuple_data]

    @staticmethod
    def createFolder(folder_name) -> None:
        """
        Create a directory (folder)

        :param folder_name: Folder or Subfolder name
        :return:
        """
        if not _op.exists(folder_name):
            os.makedirs(folder_name)
        return


if __name__ == '__main__':
    p = LoadDirectory(__file__, 'test_file', 'csv')
    print(p.getRootPath())
