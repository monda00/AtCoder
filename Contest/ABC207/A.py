a, b, c = map(int, input().split())

ans = max([a+b, a+c, b+c])

print(ans)
