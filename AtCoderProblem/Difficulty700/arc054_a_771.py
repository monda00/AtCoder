'''
[A - 動く歩道](https://atcoder.jp/contests/arc054/tasks/arc054_a)
'''

l, x, y, s, d = map(int, input().split())

if s < d:
    clockwise_dis = d - s
    counter_dis = l - clockwise_dis
else:
    clockwise_dis = (l - s) + d
    counter_dis = l - clockwise_dis

clockwise = clockwise_dis / (x + y)

if y <= x:
    ans = clockwise
else:
    counter_clockwise = counter_dis / (y - x)
    ans = min([clockwise, counter_clockwise])

print(ans)
