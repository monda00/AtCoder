n, k = map(int, input().split())
r_list = list(map(int, input().split()))

r_list.sort()
current_rate = 0
for i in range(n-k, n):
    current_rate = (current_rate + r_list[i]) / 2.0
print(current_rate)

