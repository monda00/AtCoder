n = int(input())
A = list(map(int, input().split()))

max_a = max(A)

ans = 0
max_gcd = 0
for i in range(2, max_a+1):
    tmp = 0
    for a in A:
        if a % i == 0:
            tmp += 1
    if tmp >= max_gcd:
        max_gcd = tmp
        ans = i

print(ans)
