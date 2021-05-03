import itertools

n, m, q = map(int, input().split())
con = list()
ans = 0

for _ in range(q):
    con.append(list(map(int, input().split())))

A_li = list(itertools.combinations_with_replacement(range(1,m+1),n))

for A in A_li:
    now_score = 0
    for a,b,c,d in con:
        a-=1
        b-=1
        if A[b]-A[a] == c:
            now_score += d
    ans = max(ans, now_score)

print(ans)
