'''
[C - Bugged](https://atcoder.jp/contests/abc063/tasks/arc075_a)
'''

n = int(input())
s = list()
for _ in range(n):
    s.append(int(input()))

sum_s = sum(s)

if sum_s % 10 != 0:
    print(sum_s)
    exit()

s.sort()

for sub in s:
    if (sum_s - sub) % 10 != 0:
        print(sum_s - sub)
        exit()

print(0)
