'''
[A - 点数変換](https://atcoder.jp/contests/arc043/tasks/arc043_a)
'''

n, a, b = map(int, input().split())
S = []
for _ in range(n):
    S.append(int(input()))

max_s = max(S)
min_s = min(S)

if max_s - min_s == 0:
    print(-1)
else:
    p = b / (max_s - min_s)
    q = (n * a - p * sum(S)) / n
    print(p, q)
