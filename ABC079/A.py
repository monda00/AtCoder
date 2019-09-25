n = int(input())
n_1000 = n // 1000
n_100 = (n // 100) % 10
n_10 = (n // 10) % 10
n_1 = n % 10
if n_1000 == n_100 == n_10 or n_100 == n_10 == n_1:
    print('Yes')
else:
    print('No')

