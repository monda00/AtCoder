n = int(input())
num_set = set()
ans = 0
for _ in range(n):
    tmp_input = int(input())
    if tmp_input in num_set:
        ans += 1
    else:
        num_set.add(tmp_input)

print(ans)

