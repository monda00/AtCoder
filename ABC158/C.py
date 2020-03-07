a, b = map(int, input().split())

for i in range(10001):
    a_tax = int(i * 0.08)
    b_tax = int(i * 0.1)
    if a == a_tax and b == b_tax:
        print(i)
        exit()

print(-1)
