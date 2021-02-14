'''
[A - 塗り絵](https://atcoder.jp/contests/arc051/tasks/arc051_a)
'''

import math

x1, y1, y = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

square = [[x2, y2], [x2, y3], [x3, y3], [x3, y2]]

ans_blue = "NO"
for i in range(len(square)):
    if (x1-square[i][0])**2 + (y1-square[i][1])**2 > y**2:
        ans_blue = "YES"

ans_red = "YES"
max_x = max([x2, x3])
min_x = min([x2, x3])
max_y = max([y2, y3])
min_y = min([y2, y3])
if min_x <= x1-y <= x1+y <= max_x and min_y <= y1-y <= y1+y <= max_y:
    ans_red = "NO"

print(ans_red)
print(ans_blue)
