'''
[AtCoder Regular Contest 044 - AtCoder](https://atcoder.jp/contests/arc044)

'''

import math


def is_sieve(n):
    sqrt_n = math.ceil(math.sqrt(n))
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, sqrt_n+1):
        if n % i == 0:
            return False
    return True


def is_nealy_sieve(n):
    if n == 1:
        return False
    n_li = list(map(int, str(n)))
    if n_li[-1] % 2 != 0 and n_li[-1] != 5 and sum(n_li) % 3 != 0:
        return True
    else:
        return False


n = int(input())

if is_sieve(n) or is_nealy_sieve(n):
    print('Prime')
else:
    print('Not Prime')
