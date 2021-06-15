'''
[A - Two Choices](https://atcoder.jp/contests/arc115/tasks/arc115_a)
'''

n, m = map(int, input().split())
S = []
for _ in range(n):
    S.append(input())

x = 0
y = 0
for s in S:
    if s.count('1') % 2 == 0:
        x += 1
    else:
        y += 1

print(x * y)
