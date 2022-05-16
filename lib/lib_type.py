import math
from typing import Union as _Union


class HexFloat:
    def __init__(self, hex_string_float: _Union[str, float, int]):
        self.__hex_string = hex_string_float
        if isinstance(self.__hex_string, str):
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
            print()
            if len(__str_list) == 1:
                return int(__str_list[0])
            elif len(__str_list) == 2:
                return hex(int(__str_list[0]))[2:] + '.' + hex(int(__str_list[1]))[2:] + str(len(__str_list[1]))
            else:
                raise ValueError('Invalid Number Type')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__number)

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


class HexScientificNotation:
    pass


if __name__ == '__main__':
    a = HexFloat('A.fff8')
    b = HexFloat('A')
    b1 = '37.51'
    c = HexFloat(55.5).toHexString()
    print(a, b, c, HexFloat(c), HexFloat(b1))
