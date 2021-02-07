'''
[C - 数式の書き換え](https://atcoder.jp/contests/abc033/tasks/abc033_c)
'''

s = list(input())

ans = 0
exist_zero = False
for i in range(len(s)):
    if s[i] == '0':
        exist_zero = True

    if s[i] == '+':
        if not exist_zero:
            ans += 1
        exist_zero = False

if not exist_zero:
    ans += 1

print(ans)
