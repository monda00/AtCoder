import itertools

n, k = map(int, input().split())
t = list()
for _ in range(n):
    t.append(list(map(int, input().split())))

city = [i for i in range(1, n)]

p_li = itertools.permutations(city, n-1)

ans = 0
for p in p_li:
    d = 0
    for i in range(len(p)):
        if i == 0:
            d += t[0][p[i]]
        else:
            d += t[p[i-1]][p[i]]
    d += t[p[-1]][0]

    if d == k:
        ans += 1

print(ans)
