import numpy as _np
from typing import Union as _Union
from collections import OrderedDict as _Dict


class Parser:
    def __init__(self, data_format: _Union[list, tuple, dict, set], /, *,
                 header: str = 'PSG', delimiter: str = ',', np=False) -> None:
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
        self.__use_numpy = np

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
    def reduceToN(data_list: _Union[tuple, list, dict], N: int = 50, *,
                  weight: float = 2, mode: str, avg: str = 'avg', np: str = False) -> _Union[list, _np.ndarray]:
        """
        This function reduces input list length of len(list) to N (default: 50) with weight to reduce (default: 2).
        This add options to prevent data not being seen in a graph.
        Available modes are 'cut' (Normal cutting method) and 'squeeze'.
        Available avgs are 'avg', 'avgmin', 'avgmax', and 'minmax'

        :param data_list:
        :param N:  int
        :param weight: int
        :param mode: 'cut' or 'squeeze'
        :param avg: 'avg', 'avgmin', 'avgmax' or 'minmax'
        :param np: use numpy?
        :return:
        """
        if np:
            return _np.array([])
        else:
            __data_list = data_list
            __length = len(__data_list)
            __weight = weight
            __N = N
            __avg = avg
            if __weight <= 1:
                __weight = 2
            __N_weight = int(__N // __weight)
            while __N_weight < 1:
                __N_weight += 1

            if __length <= __N:
                return __data_list
            elif __N_weight < 1:
                return __data_list[-__N:]
            else:
                if mode == 'cut':
                    return __data_list[-__N:]
                elif mode == 'squeeze':
                    if __N > 1:
                        __to_cut = __data_list[:__N_weight - __N]
                        __data_post_ = __data_list[-__N:]
                        __empty = []
                        __keep = __data_post_[__N_weight:]
                        __dpp = (__length - __N) // __N_weight
                        __delta = len(__to_cut) % __dpp
                        __idx = 0
                        if __avg == 'avg':
                            while len(__empty) < __N_weight:
                                if __idx < __N_weight - 1:
                                    __empty.append(sum(__to_cut[__idx * __dpp:(1 + __idx) * __dpp]) / __dpp)
                                else:
                                    __empty.append(sum(__to_cut[__idx * __dpp:]) / (__dpp + __delta))
                                __idx += 1
                        elif __avg == 'avgmax':
                            while len(__empty) < __N_weight:
                                if __idx < __N_weight - 1:
                                    __empty.append(sum(__to_cut[__idx * __dpp:(1 + __idx) * __dpp]) / __dpp)
                                else:
                                    __empty.append(max(__to_cut))
                                __idx += 1
                        elif __avg == 'avgmin':
                            while len(__empty) < __N_weight:
                                if __idx == 0:
                                    __empty.append(min(__to_cut))
                                elif 0 < __idx < __N_weight - 1:
                                    __empty.append(sum(__to_cut[__idx * __dpp:(1 + __idx) * __dpp]) / __dpp)
                                else:
                                    __empty.append(sum(__to_cut[__idx * __dpp:]) / (__dpp + __delta))
                                __idx += 1
                        elif __avg == 'minmax':
                            while len(__empty) < __N_weight:
                                if __idx == 0:
                                    __empty.append(min(__to_cut))
                                elif 0 < __idx < __N_weight - 1:
                                    __empty.append(sum(__to_cut[__idx * __dpp:(1 + __idx) * __dpp]) / __dpp)
                                else:
                                    __empty.append(max(__to_cut))
                                __idx += 1
                        else:
                            raise AttributeError(
                                '\'' + __avg + '\' is not in available avg. Available avgs are \'avg\', '
                                               '\'avgmin\', \'avgmax\' and \'minmax\'.')
                        return [*__empty, *__keep]
                    else:
                        return __data_list
                else:
                    raise AttributeError(
                        '\'' + mode + '\' is not in available mode. Available modes are \'cut\' and \'squeeze\'.')

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
    print(data_parser.reduceToN(list(range(1, 101)), 20, weight=2.5, mode='squeeze', avg='avgmin'))
    # print(dict_out)
