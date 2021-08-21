n = int(input())

for i in range(1000):
    if 2**i > n:
        print(i-1)
        exit()
