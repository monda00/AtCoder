'''
[C - Buy an Integer](https://atcoder.jp/contests/abc146/tasks/abc146_c)
'''

a, b, x = map(int, input().split())

upper = 10**9 + 1
lower = 0
n = 0
while (upper - lower) > 1:
    n = (upper + lower) // 2
    if (a * n) + (b * len(str(n))) <= x:
        lower = n
    else:
        upper = n

ans = n

print(ans)
