from collections import Counter

n = int(input())
A = list(map(int, input().split()))
q = int(input())
B = list()
C = list()

for i in range(q):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)

sum_a = sum(A)
c = Counter(A)
for i in range(q):
    b_num = c[B[i]]
    diff = (C[i] - B[i]) * b_num
    c[C[i]] = c[C[i]] + c[B[i]]
    c[B[i]] = 0
    sum_a = sum_a + diff
    print(sum_a)
