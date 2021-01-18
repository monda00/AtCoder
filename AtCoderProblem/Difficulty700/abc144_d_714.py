'''
[D - Water Bottle](https://atcoder.jp/contests/abc144/tasks/abc144_d)
'''

import math
import numpy as np

a, b, x = map(int, input().split())

s = x / a

if s >= (a*b)/2:
    h = ((a*b - s)*2) / a
    angle = math.degrees(math.atan2(h, a))
else:
    w = 2 * s / b
    angle = math.degrees(math.atan2(b, w))

print(angle)
