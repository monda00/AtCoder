import itertools

n = int(input())
A = list(map(int, input().split()))
A = A[:8]


rem = [[] for _ in range(200)]
for i in range(len(A)):
    A[i] = A[i] % 200

for i in range(1, min(9, n+1)):
    coms = itertools.combinations([i for i in range(1, min(9, n+1))], i)
    for com in coms:
        r = 0
        for c in com:
            r += A[c-1]
            r %= 200
        rem[r].append(com)

for r in rem:
    if len(r) > 1:
        print("Yes")
        print(len(r[0]), *r[0])
        print(len(r[1]), *r[1])
        exit()

print('No')
