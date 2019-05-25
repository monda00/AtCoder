card_num, gate_num = map(int, input().split())

ans_start, ans_end = map(int, input().split())
for _ in range(gate_num-1):
    s, e = map(int, input().split())
    if e < ans_start or ans_end < s:
        print(0)
        exit()
    elif s < ans_start and ans_start < e < ans_end:
        ans_end = e
    elif ans_start < s < ans_end and ans_end < e:
        ans_start = s
    elif ans_start == e:
        ans_end = e
    elif ans_end == s:
        ans_start = s

print(ans_end - ans_start + 1)

