import heapq

q = int(input())
query = []
for _ in range(q):
    query.append(list(map(int, input().split())))

bag = []
heapq.heapify(bag)

sum = 0
for i in range(q):
    if query[i][0] == 1:
        heapq.heappush(bag, query[i][1]-sum)
    elif query[i][0] == 2:
        sum += query[i][1]
    else:
        ball_v = heapq.heappop(bag)
        print(ball_v + sum)
