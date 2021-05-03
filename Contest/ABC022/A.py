n, s, t = map(int, input().split())
x = int(input())
count = 0
if s <= x <= t:
    count += 1
for _ in range(n-1):
    var = int(input())
    x_pre = x
    x = x_pre + var
    if s <= x <= t:
        count += 1

print(count)

