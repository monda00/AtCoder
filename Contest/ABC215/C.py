from itertools import permutations

s, k = input().split()
k = int(k)

s = list(s)

perm = []
for p in permutations(s):
    perm.append(''.join(p))

perm = list(set(perm))
perm.sort()

print(perm[k-1])
