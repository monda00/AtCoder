num, sum_yen = map(int, input().split())

for n_1000 in range(num+1):
    if 1000*n_1000 > sum_yen:
        break
    for n_5000 in range(num+1-n_1000):
        if 1000*n_1000+5000*n_5000 > sum_yen or n_1000+n_5000 > num:
            break
        for n_10000 in range(num+1-n_1000-n_5000):
            if 10000*n_10000+5000*n_5000+1000*n_1000 > sum_yen or n_10000+n_5000+n_1000 > num:
                break
            elif n_10000+n_5000+n_1000 == num and \
                    10000*n_10000+5000*n_5000+1000*n_1000 == sum_yen:
                print(str(n_10000) + ' ' + str(n_5000) + ' ' + str(n_1000))
                exit()

print('-1 -1 -1')

