left, right = map(int, input().split())

min = 2019
for i in range(left, right+1):
    for j in range(i+1, right+1):
        tmp = (i * j) % 2019
        if tmp < min:
            min = tmp
        if min == 0:
            print(min)
            exit()

print(min)

