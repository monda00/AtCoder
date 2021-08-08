n = int(input())
A = list(map(int, input().split()))
player = []
for i in range(n):
    player.append([A[i], i])

player.sort()
ans = player[-2][1]

print(ans+1)
