n = int(input())
p = list(map(int, input().split()))
li_n = [0] * 200001

l_p = len(p)
current_min = 0
for i in range(l_p):
    li_n[p[i]] = 1
    for j in range(current_min, 200001):
        if li_n[j] == 0:
            current_min = j
            print(current_min)
            break
