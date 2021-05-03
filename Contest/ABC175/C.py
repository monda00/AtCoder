x, k, d = map(int, input().split())

first_step = abs(x // d)
rem_k = k - first_step

now = x
if k < first_step:
    if x < 0:
        now = x + (d * k)
    else:
        now = x - (d * k)
else:
    if x < 0:
        now = x + (d * first_step)
        if rem_k % 2 == 1:
            if now < 0:
                now += d
            else:
                now -= d
    else:
        now = x - (d * first_step)
        if rem_k % 2 == 1:
            if now < 0:
                now += d
            else:
                now -= d

print(abs(now))
