'''
[A - Airport Bus](https://atcoder.jp/contests/agc011/tasks/agc011_a)
'''

n, c, k = map(int, input().split())
t = []
for _ in range(n):
    t.append(int(input()))

t.sort()

cap = []
ans = 0
for i in range(len(t)):
    if len(cap) == 0:
        ans += 1
        start_time = t[i]
        cap.append(t[i])
    elif t[i] - cap[0] <= k and len(cap) < c:
        cap.append(t[i])
    else:
        cap = []
        ans += 1
        start_time = t[i]
        cap.append(t[i])

print(ans)
