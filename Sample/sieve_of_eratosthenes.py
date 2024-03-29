import math

n = int(input())


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime


prime = sieve_of_eratosthenes(n)
for p in range(n+1):
    if prime[p]:
        print(p, end=' ')
print('')
print(sum(prime))
