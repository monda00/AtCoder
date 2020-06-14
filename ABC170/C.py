x, n = map(int, input().split())

if n == 0:
    print(x)
    exit()

p_li = list(map(int, input().split()))
p_li.sort()

ans = 999
for i in range(-1, 102):
    if not i in p_li:
        tmp = i

        if abs(x - ans) > abs(x - tmp):
            ans = i

print(ans)
