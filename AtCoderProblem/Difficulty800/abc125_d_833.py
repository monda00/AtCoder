'''
[D - Flipping Signs](https://atcoder.jp/contests/abc125/tasks/abc125_d)
'''

n = int(input())
A = list(map(int, input().split()))

m_num = 0
for a in A:
    if a < 0:
        m_num += 1

A_abs = []
for a in A:
    A_abs.append(abs(a))

if m_num % 2 == 0:
    ans = sum(A_abs)
else:
    ans = sum(A_abs) - 2*min(A_abs)

print(ans)
