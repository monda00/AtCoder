'''
[B - おとぎの国の高橋君](https://atcoder.jp/contests/arc009/tasks/arc009_2)
'''

b = list(map(int, input().split()))
n = int(input())
a = []
for _ in range(n):
    a.append(input())

digit_l = []

for num in a:
    s = str()
    for d in range(len(num)):
        s += str(b.index(int(num[d])))
    digit_l.append((int(s), int(num)))

digit_l.sort()
for dig in digit_l:
    print(dig[1])
