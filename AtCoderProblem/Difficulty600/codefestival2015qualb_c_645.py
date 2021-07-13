'''
[C - 旅館](https://atcoder.jp/contests/code-festival-2015-qualb/tasks/codefestival_2015_qualB_c)
'''

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

if n < m:
    print('NO')
    exit()

current_client = 0
for i in range(n):
    if m <= current_client:
        break
    if A[i] < B[current_client]:
        print('NO')
        exit()
    current_client += 1

print('YES')
