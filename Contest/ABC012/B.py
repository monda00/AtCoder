n = int(input())

hour = str(n // 3600)
rem = n % 3600
minutes = str(rem // 60)
rem = rem % 60
seconds = str(rem)

print(hour.zfill(2) + ":" + minutes.zfill(2) + ":" + seconds.zfill(2))

