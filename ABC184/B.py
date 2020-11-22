n, x = map(int, input().split())
s = input()

ans = x
for i in range(n):
    if s[i] == 'o':
        if ans < 0:
            ans = 1
        else:
            ans += 1
    else:
        ans -= 1

if ans < 0:
    print(0)
else:
    print(ans)
