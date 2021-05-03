n = int(input())
s = set()

for i in range(2, n):
    for j in range(2, n):
        if i**j > n:
            break
        s.add(i**j)
    if i**2 > n:
        break

ans = n - len(s)
print(ans)
