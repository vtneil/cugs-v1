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
    37: '37m'
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
    47: '47m'
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
    5: '5'
}


def scrollConsole() -> None:
    print('\n' * 150)
    return


def printStyled(*args, fg: _Union[int, str] = 'red', bg: _Union[int, str] = 'green', style: _Union[int, str] = None,
                end='\n') -> None:
    __str_color = '\033['
    if style is not None:
        __str_color += __color_lib_dict_style[style] + ';'
    __str_color += __color_lib_dict_fg[fg] + ';' + __color_lib_dict_bg[bg]
    print(__str_color, end='')
    print(*args, end='')
    print('\033[0;0m', end=end)
    return


def wrapper(func, args, kwargs):
    return func, args, kwargs


if __name__ == '__main__':
    printStyled('hello world', fg='red', bg='green')
    print('----')
    wrapper(scrollConsole, 1, 2)
