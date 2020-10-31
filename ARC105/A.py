import itertools

cookie = list(map(int, input().split()))
sum_cookie = sum(cookie)

if sum(cookie) == 0:
    print('Yes')
    exit()

for i in range(4):
    for conb in itertools.combinations(cookie, i):
        sum_c = sum(conb)
        if sum_c == sum_cookie - sum_c:
            print('Yes')
            exit()

print('No')
