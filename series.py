#!/usr/bin/env python3
import primes
import utils
import math


def a265326(limit=800000):
    x = []
    y = []
    p = primes.primes_up_to(limit)
    for i in p:
        binary = utils.int_to_binary(i)
        reverse = binary[::-1]
        reverse_int = utils.binary_to_int(reverse)
        n = i - reverse_int
        x.append(i)
        y.append(n)
    desc = 'A265326 - N-th prime minus its binary reversal'
    series = ', '.join(map(str, y[:20])) + ', ...'
    return x, y, desc, series


def a133058(limit=1500):
    x = []
    y = []
    x.append(0)
    x.append(1)
    y.append(1)
    y.append(1)
    for i in range(len(x), limit):
        if math.gcd(i, y[-1]) == 1:
            y.append(y[-1] + i + 1)
        else:
            y.append(int(y[-1] / math.gcd(y[-1], i)))
        x.append(i)
    desc = 'A133058 - Fly straight, dammit!'
    series = ', '.join(map(str, y[:20])) + ', ...'
    return x, y, desc, series


def a181391(limit=1000000):
    x = []
    y = []
    x.append(0)
    y.append(0)
    seen = [False for i in range(limit)]
    for i in range(len(x), limit):
        last = y[-1]
        if seen[last]:
            y.append(len(y) - seen[last] + 1)
        else:
            y.append(0)
        seen[last] = len(y)
        x.append(i)
    desc = 'A181391 - Van Eck\'s sequence'
    series = ', '.join(map(str, y[:20])) + ', ...'
    return x, y, desc, series


def main():
    # f = a265326
    f = a133058
    # f = a181391
    utils.plot(f, 'linear')


if __name__ == '__main__':
    main()
