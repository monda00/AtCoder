'''
[C - Big Array](https://atcoder.jp/contests/abc061/tasks/abc061_c)
'''

n, k = map(int, input().split())
li = []
for _ in range(n):
    a, b = map(int, input().split())
    li.append([a, b])

li.sort(key=lambda x: (x[0], x[1]))

now = 0
for l in li:
    now += l[1]
    if k <= now:
        ans = l[0]
        break

print(ans)
