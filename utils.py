#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt


def binary_to_int(n):
    return int(n, 2)


def int_to_binary(n):
    return bin(n)[2:]


def plot(f, scale='linear'):
    start = time.time()
    x, y, desc, series = f()
    end = time.time() - start
    print('%s took %f seconds for %d elements' % (f.__name__, end, len(x)))
    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111)
    plt.yscale(scale)

    # Axis labels
    fontsize = 15

    plt.title(desc + '\n' + series, fontsize=fontsize)
    ax.plot(x, y, 'ro', markersize=1)
    # ax.savefig(f.__name__ + '.svg')
    plt.show()
