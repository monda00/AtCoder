import heapq

n, m = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))

heapq.heapify(A)

for _ in range(m):
    min_price = heapq.heappop(A)
    heapq.heappush(A, (-1)*(-min_price//2))

print(-sum(A))
