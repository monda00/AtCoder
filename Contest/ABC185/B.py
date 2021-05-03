n, m, t = map(int, input().split())
A = list()
B = list()
for _ in range(m):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

rem = n
rem -= A[0]

if rem <= 0:
    print('No')
    exit()

rem += B[0] - A[0]
rem = min(rem, n)

for i in range(1, m):
    rem -= A[i] - B[i-1]
    if rem <= 0:
        print('No')
        exit()
    rem += B[i] - A[i]
    rem = min(rem, n)

rem -= t - B[-1]
if rem <= 0:
    print('No')
    exit()

print('Yes')
