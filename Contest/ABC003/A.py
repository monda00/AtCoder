n = int(input())

ans = 0
for i in range(1, n+1):
    ans += (10000 * i) * (1 / n)

print(ans)

