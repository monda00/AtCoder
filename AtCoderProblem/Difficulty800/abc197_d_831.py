'''
[D - Opposite](https://atcoder.jp/contests/abc197/tasks/abc197_d)
'''

import math

n = int(input())
x0, y0 = map(float, input().split())
x_half, y_half = map(float, input().split())

angle = 360 / n

xc = (x0 + x_half) / 2
yc = (y0 + y_half) / 2

x1 = (x0 - xc) * math.cos(math.radians(angle)) - \
     (y0 - yc) * math.sin(math.radians(angle)) + xc
y1 = (x0 - xc) * math.sin(math.radians(angle)) + \
     (y0 - yc) * math.cos(math.radians(angle)) + yc

print(x1, y1)
