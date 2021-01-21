'''
[C - Go Home](https://atcoder.jp/contests/abc056/tasks/arc070_a)
'''

x = int(input())

i = 1
now = 0
while True:
    now += i
    if now >= x:
        print(i)
        exit()
    i += 1
