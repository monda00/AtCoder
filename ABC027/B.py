n = int(input())
a_li = list(map(int, input().split()))

if sum(a_li) % n != 0:
    print(-1)
    exit()

num_island = sum(a_li) // n
bridge_num = 0
diff = 0

for i in range(n):
    diff += a_li[i] - num_island
    if diff != 0:
        bridge_num += 1
print(bridge_num)

