'''
https://www.publickey1.jp/blog/21/rpapower_automate_desktop_for_windows_10microsoft_ignite_2021.html
'''


def g1(n, p):
    if n == 0:
        return 0
    return n//p + g1(n//p, p)


def g2(n, p):
    if n % 2 == 1:
        return g1(n, p) - g2(n-1, p)

    res = g1(n//2, p)
    if p == 2:
        res += n//2
    return res


n = int(input())

ans = min(g2(n, 2), g2(n, 5))

print(ans)
