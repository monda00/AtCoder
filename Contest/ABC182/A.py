a, b = map(int, input().split())

max_follower = 2 * a + 100

ans = max_follower - b

if ans <= 0:
    print(0)
else:
    print(ans)
