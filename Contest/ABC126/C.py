import math

n, k = map(int, input().split())

ans = 0
for i in range(1, n+1):
    p = math.ceil(math.log2(k/i))
    if p >= 0:
        ans += (1/n) * ((1/2)**p)
    else:
        ans += (1/n) * 1

print(ans)

