'''
[B - 割り切れる日付](https://atcoder.jp/contests/arc002/tasks/arc002_2)
'''

import datetime

date = input()
d = date.split('/')

d = datetime.date(int(d[0]), int(d[1]), int(d[2]))

while True:
    year = d.year
    month = d.month
    day = d.day
    if (year / month) % day == 0:
        break
    d = d + datetime.timedelta(days=1)

print(d.strftime("%Y/%m/%d"))
