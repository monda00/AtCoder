n = int(input())
A = list(map(int, input().split()))
origin_A = A
tmp = list()

if len(A) == 2:
    print(A.index(min(A))+1)
    exit()

for i in range(n):
    for j in range(len(A)//2):
        if A[2*j] > A[2*j+1]:
            tmp.append(A[2*j])
        else:
            tmp.append(A[2*j+1])
    A = tmp
    tmp = list()
    if len(A) == 2:
        break

print(origin_A.index(min(A))+1)
