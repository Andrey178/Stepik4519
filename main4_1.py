import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import plotext as tpl


def task(name):
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.axis([0, 10, -1.5, 1.5])

    plt.title('Sine & Cosine')
    plt.xlabel('x')
    plt.ylabel('F(x)')

    xs = []
    sin_vals = []
    cos_vals = []

    x = 0.0
    while x < 10.0:
        sin_vals += [math.sin(3 * x)]
        cos_vals += [math.cos(x)]
        xs += [x]
        x += 0.1

    plt.plot(xs, sin_vals, color='blue', linestyle='solid',
             label='sin(3x)')
    plt.plot(xs, cos_vals, color='red', linestyle='dashed',
             label='cos(x)')

    plt.legend(loc='upper right')
    fig.savefig('trigan.png')

    tpl.plot(xs, sin_vals, color='blue')
    tpl.plot(xs, cos_vals, color='red')
    # plt2 = tpl.figure().plot(sin_vals, cos_vals, width=60, height=20)
    tpl.show()


if __name__ == '__main__':
    task('main')
