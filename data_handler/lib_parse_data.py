import numpy as _np
from typing import Union as _Union
from collections import OrderedDict as _Dict


class Parser:
    def __init__(self, data_format: _Union[list, tuple, dict, set], /, *,
                 header: str = 'PSG', delimiter: str = ',', use_np=False) -> None:
        """
        A parser object

        :param data_format: Any Iterable of data key/identifier/name
        :param header: A header of a packet to parse
        :param delimiter: A delimiter in the data to be parsed
        """
        self.__data_format = data_format
        self.__len_data_format = len(self.__data_format)
        self.__header = header
        self.__delimiter = delimiter
        self.__data_dict = dict()
        self.__is_valid = False
        self.__use_numpy = use_np

    def createBlankDataDict(self, *, ordered: bool = True) -> _Union[_Dict, dict]:
        if self.__use_numpy:
            if ordered:
                return _Dict([(k, _np.array([])) for k in self.__data_format])
            else:
                return {k: _np.array([]) for k in self.__data_format}
        else:
            if ordered:
                return _Dict([(k, []) for k in self.__data_format])
            else:
                return {k: [] for k in self.__data_format}

    def parseData(self, raw_text, /, *, ordered: bool = True) -> _Union[_Dict, dict]:
        """
        Parse a data into a dictionary of data which keys are from data format and values are from
        forced conversion to int then float then string of the parsed values.

        :param raw_text: Input raw text to be parsed
        :param ordered: Use OrderedDict?
        :return: Parsed keys values dictionary
        """
        __list_raw_text = raw_text.strip().split(self.__delimiter)
        __list_raw_text = __list_raw_text[:self.__len_data_format] + self.__len_data_format * [None]
        self.__is_valid = self.__len_data_format == len(__list_raw_text)
        if ordered:
            self.__data_dict = _Dict([(k, self.__forceConvertType(v))
                                      for k, v in zip(self.__data_format, __list_raw_text)])
        else:
            self.__data_dict = {k: self.__forceConvertType(v)
                                for k, v in zip(self.__data_format, __list_raw_text)}
        return self.__data_dict

    @staticmethod
    def __forceConvertType(value) -> _Union[int, float, str]:
        """
        Force a conversion from string to int, if not then float, if not then
        return the same string

        :param value: Input value to force-convert
        :return:
        """
        if value:
            try:
                if int(float(value)) == float(value):
                    return int(value)
                else:
                    return float(value)
            except ValueError:
                return value
        else:
            return value


if __name__ == '__main__':
    data_parser = Parser(('d1', 'd2', 'd3'))
    dict_out = data_parser.parseData('PSG,1,2,3,4,5')
    # print(dict_out)
