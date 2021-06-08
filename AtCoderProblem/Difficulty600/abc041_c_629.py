'''
[C - 背の順](https://atcoder.jp/contests/abc041/tasks/abc041_c)
'''

n = int(input())
a = list(map(int, input().split()))

A = []
for i in range(n):
    A.append([i, a[i]])

A.sort(key=lambda x: x[1], reverse=True)

for i in range(n):
    print(A[i][0]+1)
