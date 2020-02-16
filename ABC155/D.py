n, k = map(int, input().split())
a_li = list(map(int, input().split()))

a_li.sort()

rem_k = k
for i in range(1, n + 1):
    if rem_k - (n - i) < 0:
        round_index = i - 1
        break
    rem_k -= (n - i)
min_index = rem_k + 1
round_num = a_li[round_index]
del a_li[round_index]

# マイナスの値がある
if a_li[0] < 0:
    ans = round_num * a_li[-1 * (min_index + 1)]
# マイナスの値がない
else:
    ans = round_num * a_li[min_index]

print(ans)

