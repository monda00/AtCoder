def is_nth_bit_set(num, n):
    if num & (1 << n):
        return True
    else:
        return False

n, X = map(int, input().split())
a = list(map(int, input().split()))

sum_price = 0
for i in range(n):
    if is_nth_bit_set(X, i):
        sum_price += a[i]

print(sum_price)

