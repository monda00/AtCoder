import math

n = int(input())

ans = 0
x = 1
max_num = (-1 + math.sqrt(1+8*n))//2
while x <= max_num:
    if (2*n - x**2 + x) % (2 * x) == 0:
        ans += 1
    x += 1

print(ans*2)
