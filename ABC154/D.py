n, k = map(int, input().split())
p = list(map(int, input().split()))
p = [(1+x)/2 for x in p]

sub_sum = []
sub_sum.append(p[0])

for i in range(1, n):
    sub_sum.append(sub_sum[i-1]+p[i])

ans = sub_sum[k-1]

for i in range(k, n):
    ans = max(ans, sub_sum[i]-sub_sum[i-k])

print(ans)
