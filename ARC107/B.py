n, k = map(int, input().split())

ans = 0

for i in range(2, 2*n+1):
    alpha = i
    beta = alpha - k
    if beta <= 0:
        continue
    alpha_num = min(alpha-1, 2*n+1-alpha)
    beta_num = min(beta-1, 2*n+1-beta)
    if alpha_num < 0 or beta_num < 0:
        continue
    ans += alpha_num * beta_num

print(ans)
