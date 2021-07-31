n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

ai = 0
bi = 0

current_min = abs(A[ai]-B[bi])
while ai != n-1 or bi != m-1:
    tmp_min = abs(A[ai]-B[bi])
    if current_min > tmp_min:
        current_min = tmp_min

    if ai == n-1:
        bi += 1
        continue
    elif bi == m-1:
        ai += 1
        continue

    if A[ai] < B[bi]:
        ai += 1
    elif A[ai] > B[bi]:
        bi += 1
    else:
        if A[ai+1] < B[bi+1]:
            ai += 1
        elif A[ai+1] > B[bi+1]:
            bi += 1
        else:
            ai += 1
            bi += 1

print(current_min)
