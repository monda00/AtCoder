N = int(input())
L = list(map(int, input().split()))
len_l = len(L)
ans = 0

for i in range(len_l):
    for j in range(i+1, len_l):
        for k in range(j+1, len_l):
            if abs(L[i]-L[j]) < L[k] < L[i] + L[j] and L[i] != L[j] != L[k] != L[i]:
                ans += 1

print(ans)
