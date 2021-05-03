n = int(input())
n_1000 = n // 1000 + 1
ans = 1000*n_1000 - n
if ans == 1000:
    print(0)
else:
    print(ans)
