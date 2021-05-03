n, k = map(int,  input().split())
p_li = list(map(int, input().split()))

ans = 0
for i in range(k):
    min_i = min(p_li)
    p_li.remove(min_i)
    ans += min_i

print(ans)
