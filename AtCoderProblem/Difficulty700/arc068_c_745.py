'''
[C - X: Yet Another Die Game](https://atcoder.jp/contests/arc068/tasks/arc068_a)
'''

x = int(input())

ans = 0
if x <= 6:
    ans = 1
else:
    x = x - 6
    div = x // 11
    rem = x % 11
    ans = 1 + div*2
    if rem == 0:
        ans += 0
    elif rem <= 5:
        ans += 1
    else:
        ans += 2

print(ans)
