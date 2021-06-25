from itertools import permutations

n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

permutaion = list(permutations([i for i in range(1, n+1)], n))

permutaion.sort()

for i, p in enumerate(permutaion):
    if list(p) == P:
        a = i
    if list(p) == Q:
        b = i

ans = abs(a - b)

print(ans)
