import math

n = int(input())
a = list(map(int, input().split()))

bug_num = 0
bug_soft = 0
for i in range(n):
    if a[i] != 0:
        bug_num += a[i]
        bug_soft += 1

print(math.ceil(float(bug_num) / bug_soft))

