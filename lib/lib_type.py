import math
from typing import Union as _Union
import numpy as np


class HexFloat:
    def __init__(self, hex_string_float: _Union[str, float, int]):
        self.__hex_string = hex_string_float
        if isinstance(self.__hex_string, str):
            self.__hex_string = self.__hex_string.lower()
            self.__integer_num = None
            self.__decimal_num = None
            self.__decimal_len = None
            self.__hex_split = self.__hex_string.split('.')
            self.__len_inp = len(self.__hex_split)

            if self.__len_inp == 1:
                self.__integer_num = str(int(self.__hex_split[0], 16))
            elif self.__len_inp == 2:
                self.__integer_num = str(int(self.__hex_split[0], 16))
                self.__decimal_num = str(int(self.__hex_split[1][:-1], 16))
                self.__decimal_len = int(self.__hex_split[1][-1], 16)
            else:
                raise ValueError('Invalid HexFloat Input')

            if self.__decimal_num is None:
                self.__number = int(self.__integer_num)
            else:
                self.__number = float(self.__integer_num + '.' + self.__decimal_num.rjust(self.__decimal_len, '0'))

        else:
            self.__number = self.__hex_string

    def toHexString(self):
        if isinstance(self.__hex_string, str):
            return self.__hex_string
        else:
            __str_list = str(self.__number).split('.')
            if len(__str_list) == 1:
                return hex(int(__str_list[0])).replace('0x', '')
            elif len(__str_list) == 2:
                return hex(int(__str_list[0])).replace('0x', '') + '.' + \
                       hex(int(__str_list[1])).replace('0x', '') + str(len(__str_list[1]))
            else:
                raise ValueError('Invalid Number Type')

    def toNumber(self):
        return self.__number

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__number)

    def __eq__(self, other):
        if isinstance(other, HexFloat):
            return self.__number == other.__number
        else:
            return self.__number == other

    def __lt__(self, other):
        if isinstance(other, HexFloat):
            return self.__number < other.__number
        else:
            return self.__number < other

    def __gt__(self, other):
        if isinstance(other, HexFloat):
            return self.__number > other.__number
        else:
            return self.__number > other

    def __float__(self):
        return float(self.__number)

    def __int__(self):
        return int(self.__number)

    def __abs__(self):
        return abs(self.__number)

    def __bool__(self):
        return bool(self.__number)

    def __add__(self, other):
        if isinstance(other, HexFloat):
            return self.__number + other.__number
        else:
            return self.__number + other

    def __mul__(self, other):
        if isinstance(other, HexFloat):
            return self.__number * other.__number
        else:
            return self.__number * other

    def __neg__(self):
        return -self.__number

    def __hex__(self):
        return hex(self.__int__())

    def __oct__(self):
        return oct(self.__int__())

    def __ceil__(self):
        return math.ceil(self.__number)

    def __floor__(self):
        return math.floor(self.__number)

    def __copy__(self):
        return self

    def __divmod__(self, other):
        return (self.__floordiv__(other), self.__mod__(other))

    def __floordiv__(self, other):
        if isinstance(other, HexFloat):
            return self.__number // other.__number
        else:
            return self.__number // other

    def __mod__(self, other):
        if isinstance(other, HexFloat):
            return self.__number % other.__number
        else:
            return self.__number % other

    def __pow__(self, power, modulo=None):
        return self.__number ** power

    def __truediv__(self, other):
        if isinstance(other, HexFloat):
            return self.__number / other.__number
        else:
            return self.__number / other


class HexScientific:
    def __init__(self, hex_string_float: _Union[str, float, int]):
        self.__hex_string = hex_string_float
        if isinstance(self.__hex_string, str):
            self.__hex_string = self.__hex_string.lower()
            self.__mantissa = None
            self.__exponent = None
            if 'p' in self.__hex_string:
                self.__hex_split = self.__hex_string.split('p')
            else:
                self.__hex_split = [self.__hex_string, '0']
            self.__len_inp = len(self.__hex_split)

            if self.__len_inp == 2:
                self.__mantissa = int(self.__hex_split[0], 16)
                self.__exponent = -int(self.__hex_split[1], 16)
            else:
                raise ValueError('Invalid HexFloat Input')

            self.__number = self.__mantissa * 10 ** self.__exponent

        else:
            self.__number = self.__hex_string

    def toHexString(self):
        if isinstance(self.__hex_string, str):
            return self.__hex_string
        else:
            __str_list = str(self.__number).split('.')
            if len(__str_list) == 1:
                return hex(int(__str_list[0])).replace('0x', '')
            elif len(__str_list) == 2:
                __exp = len(__str_list[1])
                __mts = hex(round(self.__number * 10 ** __exp)).replace('0x', '')
                __exp_hex = hex(__exp).replace('0x', '')
                return __mts + 'p' + str(__exp_hex)

            else:
                raise ValueError('Invalid Number Type')

    def toNumber(self):
        return self.__number

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__number)

    def __eq__(self, other):
        if isinstance(other, HexScientific):
            return self.__number == other.__number
        else:
            return self.__number == other

    def __lt__(self, other):
        if isinstance(other, HexScientific):
            return self.__number < other.__number
        else:
            return self.__number < other

    def __gt__(self, other):
        if isinstance(other, HexScientific):
            return self.__number > other.__number
        else:
            return self.__number > other

    def __float__(self):
        return float(self.__number)

    def __int__(self):
        return int(self.__number)

    def __abs__(self):
        return abs(self.__number)

    def __bool__(self):
        return bool(self.__number)

    def __add__(self, other):
        if isinstance(other, HexScientific):
            return self.__number + other.__number
        else:
            return self.__number + other

    def __mul__(self, other):
        if isinstance(other, HexScientific):
            return self.__number * other.__number
        else:
            return self.__number * other

    def __neg__(self):
        return -self.__number

    def __hex__(self):
        return hex(self.__int__())

    def __oct__(self):
        return oct(self.__int__())

    def __ceil__(self):
        return math.ceil(self.__number)

    def __floor__(self):
        return math.floor(self.__number)

    def __copy__(self):
        return self

    def __divmod__(self, other):
        return (self.__floordiv__(other), self.__mod__(other))

    def __floordiv__(self, other):
        if isinstance(other, HexScientific):
            return self.__number // other.__number
        else:
            return self.__number // other

    def __mod__(self, other):
        if isinstance(other, HexScientific):
            return self.__number % other.__number
        else:
            return self.__number % other

    def __pow__(self, power, modulo=None):
        return self.__number ** power

    def __truediv__(self, other):
        if isinstance(other, HexScientific):
            return self.__number / other.__number
        else:
            return self.__number / other


def eval_eff_percent(list_in: list, factor: int = 100, dec_place: int = 2):
    if len(list_in) < 2:
        raise ValueError('Invalid list')

    return [factor, *[[round(factor * x / list_in[0], dec_place) for x in sub_list] for sub_list in list_in[1:]]]

def exp_eff_percent(name: str, list_in: list):
    if len(list_in) < 2:
        raise ValueError('Invalid list')
    return ','.join([name, *[str(x) for sub_list in list_in[1:] for x in sub_list]])

def create_sample():
    np.random.seed(6432158421 // 2)
    max_sample = [10 * x for x in range(1, 10000)]

    with open('../test/out_perf.csv', 'w') as f:
        for ms in max_sample:
            list_comp = [
                round(np.random.uniform(-x, x), np.random.randint(0, 8)) for x in range(ms)
            ]
            list_comp.extend([
                round(np.random.uniform(-x, x), np.random.randint(0, 8)) for x in range(ms)
            ])
            list_eval = []
            list_result = [0, [0, 0, 0], [0, 0, 0]]

            for x in list_comp:
                list_eval.append([
                    len(str(x)),
                    len(HexFloat(x).toHexString()),
                    len(HexScientific(x).toHexString()),
                ])

            for len_0, len_1, len_2 in list_eval:
                if len_1 > len_0:
                    list_result[1][0] += (len_1 - len_0)
                elif len_1 < len_0:
                    list_result[1][2] += (len_0 - len_1)
                else:
                    list_result[1][1] += 1

                if len_2 > len_0:
                    list_result[2][0] += (len_2 - len_0)
                elif len_2 < len_0:
                    list_result[2][2] += (len_0 - len_2)
                else:
                    list_result[2][1] += 1

                list_result[0] += 1
            out_l = eval_eff_percent(list_result, 100, 5)
            f.write(exp_eff_percent(str(ms), out_l))
            f.write('\n')


if __name__ == '__main__':
    a = HexScientific(13.123456).toHexString()
    b = HexScientific(100.567923).toHexString()
    print('{},{}'.format(a, b))
