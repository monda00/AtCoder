n, x = map(int, input().split())

if n - x >= x:
    print(x - 1)
else:
    print(n - x)

