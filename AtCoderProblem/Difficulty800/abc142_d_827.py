'''
[D - Disjoint Set of Common Divisors](https://atcoder.jp/contests/abc142/tasks/abc142_d)
'''

import math


def prime_factorize(n):
    return_list = []
    while n % 2 == 0:
        return_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_list.append(n)
    return return_list


a, b = map(int, input().split())

gcd = math.gcd(a, b)

if gcd == 1:
    print(1)
else:
    pf = prime_factorize(gcd)
    print(len(set(pf))+1)
