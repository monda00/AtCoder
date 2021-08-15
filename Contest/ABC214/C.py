n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = T.copy()

for i in range(n):
    if i == n-1:
        if ans[i] + S[i] < ans[0]:
            ans[0] = ans[i] + S[i]
    else:
        if ans[i] + S[i] < T[i+1]:
            ans[i+1] = ans[i] + S[i]

for i in range(n):
    if i == n-1:
        if ans[i] + S[i] < ans[0]:
            ans[0] = ans[i] + S[i]
    else:
        if ans[i] + S[i] < T[i+1]:
            ans[i+1] = ans[i] + S[i]

for i in range(n):
    print(ans[i])
