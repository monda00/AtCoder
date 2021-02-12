'''
[D - Logical Expression](https://atcoder.jp/contests/abc189/tasks/abc189_d)
'''

n = int(input())
S = []
for _ in range(n):
    S.append(input())

ans = 1
for i in range(n):
    if S[i] == "OR":
        ans += pow(2, i+1)

print(ans)
