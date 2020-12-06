'''
[C - Sentou](https://atcoder.jp/contests/arc073/tasks/arc073_a)
'''

n, t = map(int, input().split())
t_li = list(map(int, input().split()))

diff = list()
for i in range(n-1):
    diff.append(t_li[i+1] - t_li[i])

ans = 0
for d in diff:
    if d > t:
        ans += t
    else:
        ans += d

ans += t

print(ans)
