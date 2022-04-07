import _io
from typing import Union as _Union
from typing import IO as _IO


class PreferencesData:
    def __init__(self, pref: _Union[str, dict, _IO], format_: str='crab') -> None:
        '''
        A class to read custom preference data

        :param _pref_filename: Preference file path or name
        '''
        import json
        self.__pref = pref
        self.__format = format_
        self.__pref_dict = dict()
        self.__format_error = KeyError('Got {} as format but only accepts crab and json format.'
                                       .format(self.__format))
        self.__pref_error = TypeError('Got {} as pref but only accepts Union[str, dict, typing.IO].'
                                      .format(type(self.__pref)))
        if isinstance(self.__pref, str):
            if self.__format in ['crab', 'json']:
                try:
                    with open(self.__pref, mode='r') as _f:
                        self.__pref_dict = json.load(_f)
                except ValueError:
                    with open(self.__pref, mode='r') as _f:
                        dict_key = ''
                        for _line in _f:
                            _line_data = _line.strip()
                            if not _line_data:
                                continue
                            elif _line_data[0] in {'#'}:
                                continue
                            elif _line_data[0] in {'['}:
                                idx_endl = _line_data.rfind(']')
                                dict_key = _line_data[1:idx_endl]
                                self.__pref_dict[dict_key] = list()
                            else:
                                self.__pref_dict[dict_key].append(_line_data)
            else:
                raise self.__format_error
        elif isinstance(self.__pref, _IO):
            if self.__format == 'crab':
                with self.__pref as _f:
                    dict_key = ''
                    for _line in _f:
                        _line_data = _line.strip()
                        if not _line_data:
                            continue
                        elif _line_data[0] in {'#'}:
                            continue
                        elif _line_data[0] in {'['}:
                            idx_endl = _line_data.rfind(']')
                            dict_key = _line_data[1:idx_endl]
                            self.__pref_dict[dict_key] = list()
                        else:
                            self.__pref_dict[dict_key].append(_line_data)
            elif self.__format == 'json':
                with self.__pref as _f:
                    self.__pref_dict = json.load(_f)
            else:
                raise self.__format_error
        elif isinstance(self.__pref, dict):
            self.__pref_dict = self.__pref
        else:
            raise self.__pref_error

    def getPreferences(self) -> dict:
        '''
        Get data in tuple format.

        :return: Data in tuple format
        '''
        return self.__pref_dict

    def writePreferences(self, file_format = None) -> bool:
        '''
        Write preferences to file.
        Internal Python functions only update the preferences dictionary, but
        this method will update the file as set.

        :return: True if successful, False if failed
        '''
        __ff = file_format
        if not __ff:
            __ff = self.__format
        if isinstance(self.__pref, str):
            if __ff == 'crab':
                try:
                    with open(self.__pref, mode='w') as _f:
                        for line in self.__generateCrabFileFormat(self.__pref_dict):
                            _f.write(line)
                            _f.write('\n')
                    return True
                except Exception:
                    return False
            elif __ff == 'json':
                import json
                try:
                    __json_obj = json.dumps(self.__pref_dict, indent=4)
                    with open(self.__pref, mode='w') as _f:
                        _f.write(__json_obj)
                    return True
                except Exception:
                    return False
        elif isinstance(self.__pref, _IO):
            if __ff == 'crab':
                try:
                    with self.__pref as _f:
                        for line in self.__generateCrabFileFormat(self.__pref_dict):
                            _f.write(line)
                            _f.write('\n')
                    return True
                except Exception:
                    return False
            elif __ff == 'json':
                import json
                try:
                    __json_obj = json.dumps(self.__pref_dict, indent=4)
                    with self.__pref as _f:
                        _f.write(__json_obj)
                    return True
                except Exception:
                    return False
        elif isinstance(self.__pref, dict):
            return False
        else:
            raise self.__format_error

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
    def __generateCrabFileFormat(inp_dict: dict):
        for k, v in inp_dict.items():
            yield '[' + str(k) + ']'
            for elem in v:
                yield str(elem)
            yield ''

if __name__ == '__main__':
    f = open('data_format.txt')
    with f:
        for line in f:
            print(line)
