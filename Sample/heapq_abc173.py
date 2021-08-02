import heapq

n = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 0
que = []
heapq.heappush(que, -A[0])
for i in range(1, n):
    friendly = heapq.heappop(que) * (-1)
    ans += friendly
    heapq.heappush(que, -A[i])
    heapq.heappush(que, -A[i])

print(ans)
