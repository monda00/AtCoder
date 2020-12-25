'''
[A - Two Abbreviations](https://atcoder.jp/contests/agc028/tasks/agc028_a)
'''

import math

n, m = map(int, input().split())
s = list(input())
t = list(input())
l = (n * m) // math.gcd(n, m)
gcd = math.gcd(n, m)

for i in range(gcd):
    if s[i*(n//gcd)] != t[i*(m//gcd)]:
        print(-1)
        exit()

print(l)
