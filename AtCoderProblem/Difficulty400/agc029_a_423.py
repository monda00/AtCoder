S = input()

w_num = 0
ans = 0
for i in range(len(S)):
    if S[i] == 'W':
        ans += (i - w_num)
        w_num += 1

print(ans)
