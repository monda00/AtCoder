a, b = map(int, input().split())

ans = b - a + 1

if ans < 0:
    ans = 0

print(ans)
