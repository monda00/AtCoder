'''
[B - Evilator](https://atcoder.jp/contests/agc015/tasks/agc015_b)
'''
s = list(input())
len_s = len(s)

ans = 0
for i in range(len_s):
    if s[i] == 'U':
        ans += (i * 2) + (len_s - i - 1)
    else:
        ans += i + ((len_s - i - 1) * 2)

print(ans)
