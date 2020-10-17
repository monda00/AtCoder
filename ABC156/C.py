n = int(input())
x = list(map(int, input().split()))

min_dis = 99999999
for i in range(101):
    current_dis = 0
    for j in range(n):
        current_dis += (x[j]-i)**2
    if current_dis < min_dis:
        min_dis = current_dis

print(min_dis)
