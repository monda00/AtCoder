'''
[C - 一次元リバーシ](https://atcoder.jp/contests/abc047/tasks/arc063_a)
'''

S = list(input())
len_s = len(S)

ans = 0

now = S[0]
for i in range(len_s):
    if S[i] != now:
        ans += 1
        now = S[i]

print(ans)
