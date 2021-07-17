from collections import Counter, deque

n, k = map(int, input().split())
c = list(map(int, input().split()))

select_c = c[:k]
counter_c = Counter(select_c)
pre_num = len(list(set(select_c)))
current_max = pre_num
que = deque(select_c)

for i in range(1, n-k+1):
    first = que.popleft()
    if counter_c[first] == 1:
        counter_c[first] = 0
        pre_num -= 1
    else:
        counter_c[first] -= 1
    if counter_c[c[i+k-1]]:
        if counter_c[c[i+k-1]] == 0:
            counter_c[c[i+k-1]] = 1
            pre_num += 1
        elif counter_c[c[i+k-1]] >= 1:
            counter_c[c[i+k-1]] += 1
    else:
        counter_c[c[i+k-1]] = 1
        pre_num += 1
    que.append(c[i+k-1])
    if current_max < pre_num:
        current_max = pre_num

print(current_max)
