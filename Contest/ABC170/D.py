from collections import Counter

n = int(input())
A = list(map(int, input().split()))
A.sort()
max_a = A[-1] + 1
count_a = Counter(A)
dp = [True for i in range(max_a)]
ans = 0

for a in A:
    if dp[a] and count_a[a] == 1:
        ans += 1

    for j in range(a*2, max_a, a):
        dp[j] = False

print(ans)
