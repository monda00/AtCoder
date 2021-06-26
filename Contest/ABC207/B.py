a, b, c, d = map(int, input().split())

if d * c - b == 0:
    ans = -1
elif a // (d * c - b) < 0:
    ans = -1
else:
    if a % (d * c - b) == 0:
        ans = a // (d * c - b)
    else:
        ans = a // (d * c - b)+1
print(ans)
