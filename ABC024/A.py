a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

pay_sum = a * s + b * t
if s + t >= k:
    pay_sum -= c * (s + t)

print(pay_sum)

