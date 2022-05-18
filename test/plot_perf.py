import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.interpolate import CubicSpline


if __name__ == '__main__':
    inp_data = np.genfromtxt('out_perf.csv', delimiter=',')

    x_range = np.arange(-1000, 35000, 5000)
    y_range = np.arange(-60, 40, 5)

    x_f = inp_data[:, 0]
    y_f1_neg = -inp_data[:, 1]
    y_f1_zero = inp_data[:, 2]
    y_f1_pos = inp_data[:, 3]
    y_f2_neg = -inp_data[:, 4]
    y_f2_zero = inp_data[:, 5]
    y_f2_pos = inp_data[:, 6]

    # DELTA AVERAGE
    # print(np.average(np.abs(y_f1_neg - y_f2_neg)))
    # print(np.average(np.abs(y_f1_pos - y_f2_pos)))

    # TOTAL AVERAGE
    print(np.average(y_f1_neg))
    print(np.average(y_f1_zero))
    print(np.average(y_f1_pos))
    print(np.average(y_f2_neg))
    print(np.average(y_f2_zero))
    print(np.average(y_f2_pos))

    plt.figure(figsize=(16, 20))

    plt.plot(x_f, y_f1_pos, 'b-',
             label='HexFloat +')
    plt.plot(x_f, y_f1_neg, 'b-',
             label='HexFloat -')
    plt.plot(x_f, y_f2_pos, 'r-',
             label='HexScientific +')
    plt.plot(x_f, y_f2_neg, 'r-',
             label='HexScientific -')


    plt.axhline(0, color='black')

    plt.tick_params(axis='both', which='both', length=0)
    plt.yticks(y_range)
    plt.xticks(x_range)

    plt.legend()

    # plt.show()
