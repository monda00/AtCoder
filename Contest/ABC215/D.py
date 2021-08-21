import math

n, m = map(int, input().split())
A = list(map(int, input().split()))


def factorization(num):
    fact = []
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            while num % i == 0:
                num //= i
            fact.append(i)

    if num != 1:
        fact.append(num)

    return fact


m_li = [True for _ in range(m+1)]
m_li[0] = False


for i in range(n):
    fact = factorization(A[i])
    for f in fact:
        if f <= m:
            if m_li[f]:
                for j in range(f, m+1, f):
                    m_li[j] = False

print(sum(m_li))
for i in range(m+1):
    if m_li[i]:
        print(i)
