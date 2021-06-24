import math

a, b = map(int, input().split())


def segment_sieve(a, b):
    sqrt_b = math.ceil(math.sqrt(b))
    prime_small = [True for i in range(sqrt_b)]
    prime = [True for i in range(b-a+1)]

    for i in range(2, sqrt_b):
        if prime_small[i]:
            for j in range(2*i, sqrt_b, i):
                prime_small[j] = False
            for j in range((a+i-1)//i*i, b+1, i):
                print('j: ', j)
                prime[j-a] = False

    return prime


seg_prime = segment_sieve(a, b)
for p in range(b-a+1):
    if seg_prime[p]:
        print(p+a)

print(sum(seg_prime))
