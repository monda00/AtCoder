'''
[A - Simple Calculator](https://atcoder.jp/contests/agc008/tasks/agc008_a)
'''

x, y = map(int, input().split())

if x > 0 and y > 0:
    if abs(x) > abs(y):
        ans = abs(x) - abs(y) + 2
    elif abs(x) == abs(y):
        ans = 0
    else:
        ans = abs(y) - abs(x)
elif x < 0 and y < 0:
    if abs(x) > abs(y):
        ans = abs(x) - abs(y)
    elif abs(x) == abs(y):
        ans = 0
    else:
        ans = abs(y) - abs(x) + 2
else:
    if x == y == 0:
        ans = 0
    elif x == 0:
        if y < 0:
            ans = abs(y) + 1
        else:
            ans = abs(y)
    elif y == 0:
        if x < 0:
            ans = abs(x)
        else:
            ans = abs(x) + 1
    elif abs(x) == abs(y):
        ans = 1
    elif abs(x) > abs(y):
        ans = abs(x) - abs(y) + 1
    else:
        ans = abs(y) - abs(x) + 1

print(ans)
