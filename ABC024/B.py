n, t = map(int, input().split())
a_pre = int(input())
sum_time = 0
for _ in range(n-1):
    a = int(input())
    if a - a_pre > t:
        sum_time += t
    else:
        sum_time += a - a_pre
    a_pre = a
print(sum_time + t)

