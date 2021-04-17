'''
[B - Template Matching](https://atcoder.jp/contests/abc054/tasks/abc054_b)
'''

n, m = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(list(input()))

for _ in range(m):
    B.append(list(input()))

for k in range(n-m+1):
    for i in range(n-m+1):
        for j in range(m):
            if A[j+k][i:i+m] != B[j][:]:
                break
            if j == m-1:
                print('Yes')
                exit()

print('No')
