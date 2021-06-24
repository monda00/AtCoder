import math

n = int(input())


def factorization(n):
    fact = []
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            fact.append([i, cnt])

    if n != 1:
        fact[n] = 1

    return fact


print(factorization(n))
