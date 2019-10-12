s = list(input())
n = int(input())
for _ in range(n):
    start_rev, end_rev = map(int, input().split())
    sub_str = s[start_rev-1:end_rev]
    s[start_rev-1:end_rev] = sub_str[::-1]
print("".join(s))

