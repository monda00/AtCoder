n = int(input())
p_li = list(map(int, input().split()))

answer = 0
now_min = 999999
for i in range(len(p_li)):
    if now_min > p_li[i]:
        now_min = p_li[i]
        answer += 1

print(answer)

