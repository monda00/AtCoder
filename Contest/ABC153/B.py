h, n = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) < h:
    print('No')
else:
    print('Yes')
