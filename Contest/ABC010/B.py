n = int(input())
a_li = list(map(int, input().split()))

success_ptn = [9, 7, 3, 1]

ans = 0
for a in a_li:
    for ptn in success_ptn:
        if a < ptn:
            continue
        elif a == ptn:
            break
        else:
            ans += (a - ptn)
            break

print(ans)

