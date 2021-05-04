'''
[C - Scc Puzzle](https://atcoder.jp/contests/arc069/tasks/arc069_a)
'''

n, m = map(int, input().split())

ans = 0
if n*2 <= m:
    ans = n
    m -= n*2
    n = 0
else:
    ans = m//2
    n -= m//2
    m -= m//2*2

ans += m//4

print(ans)
