bound_num, line_length = map(int, input().split())
l = list(map(int, input().split()))

bound = 1
length_sum = 0
for i in range(bound_num + 1):
    if(i == bound_num):
        print(len(l)+1)
        exit()
    if(length_sum + l[i] <= line_length):
        bound += 1
    else:
        print(bound)
        exit()
    length_sum += l[i]

