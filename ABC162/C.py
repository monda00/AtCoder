from math import gcd
from itertools import permutations

k = int(input())
ans = 0

for i in range(1, k+1):
    for j in range(i, k+1):
        for l in range(j, k+1):
            dup = len(set([i, j, l]))
            if dup == 1:
                num = 1
            elif dup == 2:
                num = len(list(permutations([i, j, l]))) / 2
            else:
                num = len(list(permutations([i, j, l])))
            ans += gcd(i, gcd(j, l)) * num

print(int(ans))
