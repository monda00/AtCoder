h, w = map(int, input().split())
S = []
for _ in range(h):
    s = list(input())
    S.append(s)

ans = 0

for i in range(h-1):
    for j in range(w-1):
        round_cell = [S[i][j], S[i][j+1], S[i+1][j], S[i+1][j+1]]
        ans += round_cell.count('#') % 2

print(ans)
