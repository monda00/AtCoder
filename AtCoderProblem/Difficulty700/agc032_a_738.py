'''
[A - Limited Insertion](https://atcoder.jp/contests/agc032/tasks/agc032_a)
'''

n = int(input())
b = list(map(int, input().split()))

a = []
while len(b) > 0:
    for i in range(len(b)-1, -1, -1):
        if b[i] == i+1:
            a.insert(0, b[i])
            b.remove(b[i])
            break
        if i == 0:
            print(-1)
            exit()

for a_i in a:
    print(a_i)
