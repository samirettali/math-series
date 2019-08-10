#!/usr/bin/env python3
import math


def is_prime(n):
    limit = math.ceil(math.sqrt(n)) + 1
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    noprimes = set(j for i in range(2, int(math.sqrt(n) + 1)) for j in range(i*2, n, i))
    primes = [x for x in range(2, n) if x not in noprimes]
    return primes

