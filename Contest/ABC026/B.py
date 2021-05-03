import math

n = int(input())
r_list = list()
for _ in range(n):
    r_list.append(int(input()))

r_list.sort(reverse=True)
area = 0
for (i, r) in enumerate(r_list):
    if i % 2 == 0:
        area += r * r * math.pi
    else:
        area -= r * r * math.pi
print(area)

