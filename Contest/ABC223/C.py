n = int(input())
A = []
B = []
sum_t = 0
for _ in range(n):
    a, b = map(int, input().split())
    sum_t += a / b
    A.append(a)
    B.append(b)

at_t = sum_t / 2
ans = 0

for i in range(n):
    if at_t > A[i]/B[i]:
        at_t -= A[i]/B[i]
        ans += A[i]
    else:
        ans += A[i] * (at_t / (A[i]/B[i]))
        break

print(ans)
