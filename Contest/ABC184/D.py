_a, _b, _c = map(int, input().split())
dp = [[[[] for _ in range(101)] for _ in range(101)] for _ in range(101)]


def f(a, b, c):
    if dp[a][b][c]:
        return dp[a][b][c]
    if a == 100 or b == 100 or c == 100:
        return 0
    ans = 0
    ans += (f(a+1, b, c)+1)*a/(a+b+c)
    ans += (f(a, b+1, c)+1)*b/(a+b+c)
    ans += (f(a, b, c+1)+1)*c/(a+b+c)
    dp[a][b][c] = ans
    return ans


ans = f(_a, _b, _c)
print(ans)
