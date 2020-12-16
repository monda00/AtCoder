'''
[A - A+...+B Problem](https://atcoder.jp/contests/agc015/tasks/agc015_a)
'''

n, a, b = map(int, input().split())

if a > b or b - a > n:
    ans = 0
else:
    ans = (n-2) * (b - a) + 1

print(ans)
