n, a, x, y = map(int, input().split())

ans = 0
if n <= a:
    ans = n * x
else:
    ans = x * a + y * (n - a)

print(ans)
