n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = list()
good_hill = set()
vt = [set() for _ in range(n)]
ans = 0

for _ in range(m):
    ab.append(list(map(int, input().split())))

for i in range(m):
    vt[ab[i][0]-1].add(ab[i][1]-1)
    vt[ab[i][1]-1].add(ab[i][0]-1)

for i in range(n):
    max_around = 0
    for v in vt[i]:
       if max_around < h[v]:
           max_around = h[v]
    if h[i] > max_around:
        ans += 1

print(ans)
