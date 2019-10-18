n, a, b = map(int, input().split())
d_sum = 0
for _ in range(n):
    s, d = input().split()
    if int(d) < a:
        d = a
    elif int(d) > b:
        d = b
    else:
        d = int(d)

    if s == 'East':
        d_sum += d
    else:
        d_sum -= d

if d_sum < 0:
    print('West', abs(d_sum))
elif d_sum > 0:
    print('East', abs(d_sum))
else:
    print(0)

