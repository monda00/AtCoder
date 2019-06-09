n = int(input())
weights = list(map(int, input().split()))

min_diff = 100000
for i in range(1, n):
    s1 = sum(weights[:i])
    s2 = sum(weights[i:])
    diff = abs(s1 - s2)
    if(min_diff > diff):
        min_diff = diff

print(min_diff)

