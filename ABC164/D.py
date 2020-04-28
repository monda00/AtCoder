s = input()[::-1]
n = len(s)
x = 1
tot = 0 # 累積和
cnt = [0 for i in range(2019)] # 累積和の値になる個数

ans = 0
for i in range(n):
    # print('======={}======'.format(i))
    cnt[tot] += 1
    tot += int(s[i])*x
    # print(tot)
    tot %= 2019
    # print(tot)
    ans += cnt[tot]
    # print('ans:', ans)
    x = x*10%2019

print(ans)
