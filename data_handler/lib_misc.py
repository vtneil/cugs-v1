import numpy as _np
from typing import Union as _Union

__color_lib_dict_fg = {
    'none': '0',
    'black': '30',
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'purple': '35',
    'cyan': '36',
    'white': '37',
    0: '0m',
    30: '30m',
    31: '31m',
    32: '32m',
    33: '33m',
    34: '34m',
    35: '35m',
    36: '36m',
    37: '37m',
    None: '0'
}

__color_lib_dict_bg = {
    'none': '0m',
    'black': '40m',
    'red': '41m',
    'green': '42m',
    'yellow': '43m',
    'blue': '44m',
    'purple': '45m',
    'cyan': '46m',
    'white': '47m',
    0: '0m',
    40: '40m',
    41: '41m',
    42: '42m',
    43: '43m',
    44: '44m',
    45: '45m',
    46: '46m',
    47: '47m',
    None: '0m'
}

__color_lib_dict_style = {
    'bold': '1',
    'bd': '1',
    'underline': '2',
    'ul': '2',
    'negative1': '3',
    'neg1': '3',
    'negative2': '5',
    'neg2': '5',
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    5: '5',
}


def scrollConsole() -> None:
    print('\n' * 150)
    return


def strStyled(*args, fg: _Union[int, str] = None, bg: _Union[int, str] = None, style: _Union[int, str] = None,
              end='\n') -> str:
    __str_color = '\033['
    if style is not None:
        __str_color += __color_lib_dict_style[style] + ';'
    __str_color += __color_lib_dict_fg[fg] + ';' + __color_lib_dict_bg[bg]
    for __args in args:
        __str_color += str(__args)
    __str_color += '\033[0;0m' + end
    return __str_color


def printStyled(*args, fg: _Union[int, str] = None, bg: _Union[int, str] = None, style: _Union[int, str] = None,
                end='\n') -> None:
    print(strStyled(*args, fg=fg, bg=bg, style=style, end=end), end='')
    return


def wrapper(func, /, *args, **kwargs):
    __return_args = []
    __return_kwargs = {}
    if args:
        __return_args = [*args]
    if kwargs:
        __return_kwargs = kwargs
    return func, __return_args, __return_kwargs


def reduceToN(data_list: _Union[tuple, list, dict, _np.ndarray], N: int = 50, *,
              weight: float = 2, mode: str, avg: str = 'avg') -> _Union[list, _np.ndarray]:
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
    if isinstance(data_list, _np.ndarray):
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


if __name__ == '__main__':
    printStyled('hello world', fg='red', bg='green')
    print('----')
    wrapper(scrollConsole, 1, 2)
