import json as _json
import toml as _toml
import yaml as _yaml
import strictyaml as _strictyaml
import xmltodict as _xmldict
import dict2xml as _dictxml
import xml as _xml
from typing import Union as _Union
from collections import OrderedDict as _Dict
from io import StringIO as _String
from lib.lib_log import Log


class PreferencesData:
    def __init__(self, pref: _Union[str, dict], /, *, mode: str = 'file') -> None:
        """
        A class to read custom preference data

        :param pref: Preference file path or name
        """
        self.__pref = pref
        self.__mode = mode
        self.__format = ''
        self.__pref_dict = dict()
        self.__format_error = KeyError('Got {} as format but only accepts json, yaml, xml and toml formats.'
                                       .format(self.__format))
        self.__pref_error = TypeError('Got {} as pref but only accepts Union[str, dict].'
                                      .format(type(self.__pref)))
        self.__format_parser = {'json': self.parseJSON,
                                'toml': self.parseTOML,
                                'xml': self.parseXML,
                                'yaml': self.parseYAML}
        self.__format_writer = {'json': self.writeJSON,
                                'toml': self.writeTOML,
                                'xml': self.writeXML,
                                'yaml': self.writeYAML}
        self.logger = Log(target='PREF_LOADER')

        if isinstance(self.__pref, str):
            if '.' in self.__pref:
                __idx_dot = self.__pref.rfind('.')
                self.__format = self.__pref[__idx_dot+1:].lower()
                self.logger.debug('Extension found: ' + self.__format)

            if self.__format and self.__format in ['json', 'toml', 'xml', 'yaml']:
                self.__pref_dict = self.__format_parser[self.__format](self.__pref, mode=self.__mode)
                self.logger.debug('Extension correct: ' + self.__format)

            else:
                try:
                    self.__pref_dict = self.parseJSON(self.__pref, mode=self.__mode)
                    self.__format = 'json'
                    self.logger.info('Preferences format is JSON. Using JSON Loader.')
                    self.logger.info('Loaded JSON as dictionary')
                except ValueError or _json.decoder.JSONDecodeError:
                    pass

                try:
                    self.__pref_dict = self.parseTOML(self.__pref, mode=self.__mode)
                    self.__format = 'toml'
                    self.logger.info('Preferences format is TOML. Using TOML Loader.')
                    self.logger.info('Loaded TOML as dictionary')
                except ValueError or _toml.decoder.TomlDecodeError:
                    pass

                try:
                    self.__pref_dict = self.parseXML(self.__pref, mode=self.__mode)
                    self.__format = 'xml'
                    self.logger.info('Preferences format is XML. Using XML Tree Loader.')
                    self.logger.info('Loaded XML as dictionary')
                except ValueError or _xml.parsers.expat.ExpatError:
                    pass

                try:
                    self.__pref_dict = self.parseYAML(self.__pref, mode=self.__mode)
                    self.__format = 'yaml'
                    self.logger.info('Preferences format is YAML. Using YAML Loader.')
                    self.logger.info('Loaded YAML as dictionary')
                except Exception:
                    raise self.__format_error

        elif isinstance(self.__pref, dict):
            self.__pref_dict = self.__pref
        else:
            raise self.__pref_error
        if not self.__format:
            self.__format = 'json'

    def getPreferences(self) -> dict:
        """
        Get data in tuple format.

        :return: Data in tuple format
        """
        return self.__pref_dict

    def writePreferences(self, pref_dict=None, pref_file_name=None, file_format=None) -> bool:
        """
        Write preferences to file.
        Internal Python functions only update the preferences dictionary, but
        this method will update the file as set.

        :return: True if successful, False if failed
        """
        if file_format is None:
            __file_format = self.__format
        else:
            __file_format = file_format.lower()

        if pref_dict is None:
            __pref = self.__pref_dict
        else:
            __pref = pref_dict

        if pref_file_name is None:
            __pref_file_name = self.__pref
        else:
            __pref_file_name = pref_file_name

        if not isinstance(__pref_file_name, str):
            raise TypeError('File name only supports \'str\' not \'' + str(type(__pref_file_name)) + '\'')

        if __file_format and __file_format in ['json', 'toml', 'xml', 'yaml']:
            self.__pref_dict = self.__format_writer[self.__format](__pref, __pref)
            return True
        return False

    def setdefault(self, key, value):
        self.__pref_dict.setdefault(key, value)

    def __len__(self) -> int:
        return len(self.__pref_dict)

    def __getitem__(self, item):
        return self.__pref_dict[item]

    def __setitem__(self, key, value):
        self.__pref_dict[key] = value
        return

    def __add__(self, other):
        for key in other:
            if key in self.__pref_dict:
                self.__pref_dict[key].extend(other[key])
            else:
                self.__pref_dict[key] = other[key]
        return

    def __sub__(self, other):
        for key in other:
            if key in self.__pref_dict:
                for elem in other[key]:
                    if elem in self.__pref_dict[key]:
                        self.__pref_dict[key].remove(elem)
        return

    def __str__(self):
        __s_out = str()
        for k, v in self.__pref_dict.items():
            __s_out += str(k) + ':' + '\n'
            for elem in v:
                __s_out += ' ' * 4 + str(elem) + '\n'
        return __s_out

    def __repr__(self):
        return str(self)

    @staticmethod
    def parseJSON(inp_str: str, /, mode: str = 'str') -> dict:
        if mode == 'str':
            return _json.loads(inp_str)
        elif mode == 'file':
            with open(inp_str, mode='r', encoding='utf-8') as __f:
                return _json.load(__f)
        else:
            raise KeyError('mode only supports str and file!')

    @staticmethod
    def parseTOML(inp_str: str, /, mode: str = 'str') -> dict:
        if mode == 'str':
            return _toml.loads(inp_str)
        elif mode == 'file':
            with open(inp_str, mode='r', encoding='utf-8') as __f:
                return _toml.load(__f)
        else:
            raise KeyError('mode only supports str and file!')

    @staticmethod
    def parseXML(inp_str: str, /, mode: str = 'str', *, disorder: bool = True) -> dict:
        if mode == 'str':
            if disorder:
                return PreferencesData.disorderDict(_xmldict.parse(inp_str, encoding='utf-8'))
            else:
                return _xmldict.parse(inp_str, encoding='utf-8')
        elif mode == 'file':
            with open(inp_str, mode='r', encoding='utf-8') as __f:
                if disorder:
                    return PreferencesData.disorderDict(_xmldict.parse(''.join(__f.readlines()), encoding='utf-8'))
                else:
                    return _xmldict.parse(''.join(__f.readlines()), encoding='utf-8')

    @staticmethod
    def parseYAML(inp_str: str, /, mode: str = 'str', *, strict_validate: bool = False) -> dict:
        if strict_validate:
            if mode == 'str':
                __f = _String(inp_str)
                return _strictyaml.load(__f)
            elif mode == 'file':
                with open(inp_str, mode='r', encoding='utf-8') as __f:
                    return _strictyaml.load(__f)
        else:
            if mode == 'str':
                __f = _String(inp_str)
                return _yaml.safe_load(__f)
            elif mode == 'file':
                with open(inp_str, mode='r', encoding='utf-8') as __f:
                    return _yaml.safe_load(__f)
            else:
                raise KeyError('mode only supports str and file!')

    @staticmethod
    def writeJSON(pref_to_write: dict, inp_file_dir: str, *, _indent: int = 4) -> bool:
        if pref_to_write:
            with open(inp_file_dir, mode='w', encoding='utf-8') as __f:
                _json.dump(pref_to_write, __f, indent=_indent)
            return True
        return False

    @staticmethod
    def writeTOML(pref_to_write: dict, inp_file_dir: str, *, _indent: int = 4) -> bool:
        if pref_to_write:
            with open(inp_file_dir, mode='w', encoding='utf-8') as __f:
                _toml.dump(pref_to_write, __f)
            return True
        return False

    @staticmethod
    def writeXML(pref_to_write: dict, inp_file_dir: str, *, _indent: int = 4) -> bool:
        if pref_to_write:
            with open(inp_file_dir, mode='w', encoding='utf-8') as __f:
                __s = _dictxml.dict2xml(pref_to_write)
                __f.writelines(s)
            return True
        return False

    @staticmethod
    def writeYAML(pref_to_write: dict, inp_file_dir: str, *, _indent: int = 4) -> bool:
        if pref_to_write:
            with open(inp_file_dir, mode='w', encoding='utf-8') as __f:
                __s = _yaml.dump(pref_to_write)
                __f.writelines(__s)
            return True
        return False

    @staticmethod
    def disorderDict(inp_dict: _Union[dict, _Dict]) -> dict:
        return _json.loads(_json.dumps(inp_dict))


if __name__ == '__main__':
    f = open('cugs_preferences.json')
    f.close()
    # s = PreferencesData.parseXML('<EmpData><EmpID>12345</EmpID><EmpName>Vivatsathorn</EmpName></EmpData>', mode='str')
    s = PreferencesData.parseYAML('hello:\n    - image\n    - command', strict_validate=False)
    ptr = {'x': {'hello': 'image', 'tt': 'command', 'qq': ['jkdashifk', 'dghsdhfj']}}
    PreferencesData.writeJSON(ptr, 'unused_file_write_test/writejson')
    print(PreferencesData.parseJSON('unused_file_write_test/writejson', 'file'))

    PreferencesData.writeTOML(ptr, 'unused_file_write_test/writetoml')
    print(PreferencesData.parseTOML('unused_file_write_test/writetoml', 'file'))

    PreferencesData.writeXML(ptr, 'unused_file_write_test/writexml')
    print(PreferencesData.parseXML('unused_file_write_test/writexml', 'file'))

    PreferencesData.writeYAML(ptr, 'unused_file_write_test/writeyaml')
    print(PreferencesData.parseYAML('unused_file_write_test/writeyaml', 'file'))
