n, k = map(int, input().split())

a = n
for i in range(k):
    g = list(str(a))
    g1 = int(''.join(sorted(g, reverse=True)))
    g2 = int(''.join(sorted(g)))
    a = g1 - g2

print(a)
