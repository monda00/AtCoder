a, b, n = map(int, input().split())

x = min(b-1, n)
ans = (a*x - (a*x%b))/b - a * ((x-(x%b))/b)

print(int(ans))
