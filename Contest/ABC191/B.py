n, x = map(int, input().split())
A = list(map(int, input().split()))

ans = [a for a in A if a != x]

print(*ans)
