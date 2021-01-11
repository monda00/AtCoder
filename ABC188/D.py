n, C = map(int, input().split())
event = list()
for _ in range(n):
    a, b, c = map(int, input().split())
    event.append((a-1, c))
    event.append((b, -c))

event.sort()

ans = 0
sum_fee = 0
t = 0
for x, y in event:
    if x != t:
        ans += min(C, sum_fee) * (x - t)
        t = x
    sum_fee += y

print(ans)
