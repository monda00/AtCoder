n = list(input())

sum_n = 0
for i in range(len(n)):
    sum_n += int(n[i])

if sum_n % 9 == 0:
    print('Yes')
else:
    print('No')
