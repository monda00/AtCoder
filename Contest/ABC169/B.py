n = int(input())
a_li = list(map(int, input().split()))

if 0 in a_li:
    print(0)
    exit()

ans = 1
a_li = [a for a in a_li if a != 1 and a != 0]
a_li.append(1)
for a in a_li:
    ans *= a
    if ans > 1000000000000000000:
        print(-1)
        exit()
print(ans)
