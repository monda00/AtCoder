import math

a = int(input())
b = int(input())
n = int(input())

ab_lcm = int(a * b / math.gcd(a, b))

for i in range(20000):
    if ab_lcm * i >= n:
        print(ab_lcm * i)
        exit()

