import math

coin_num = int(input())
coin_li = list()
for _ in range(coin_num):
    coin_li.append(int(input()))

ans = 0
for i in range(len(coin_li)):
    divisor_sum = 0
    for j in range(len(coin_li)):
        if i != j and coin_li[i] % coin_li[j] == 0:
            divisor_sum += 1
    if divisor_sum % 2 == 1:
        ans += 1/2.0
    else:
        ans += (divisor_sum + 2.0) / (2 * divisor_sum + 2.0)

print(ans)

