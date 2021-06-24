import math

n = int(input())


def is_prime(n):
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True


print(is_prime(n))
