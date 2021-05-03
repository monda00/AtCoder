n, m = map(int, input().split())
n_d = 30.0 * (n % 12) + (m / 2.0)
m_d = 6.0 * m
d = abs(n_d - m_d)
if d > 180:
    if n_d > m_d:
        d = m_d + (360 - n_d)
    else:
        d = n_d + (360 - m_d)
print(d)

