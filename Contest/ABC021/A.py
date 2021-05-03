n = int(input())
pow_li = [8, 4, 2, 1]
ans = list()
for p in pow_li:
    r = n // p
    for _ in range(r):
        ans.append(p)
        n -= p
print(len(ans))
for i in ans:
    print(i)

