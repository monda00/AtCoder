n = int(input())
k = int(input())
x = int(input())
y = int(input())
pay_sum = 0
for i in range(1, n+1):
    if i > k:
        pay_sum += y
    else:
        pay_sum += x
print(pay_sum)

