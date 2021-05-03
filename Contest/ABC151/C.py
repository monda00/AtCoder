problem_num, sub_num = map(int, input().split())
ac = 0
wa = 0
rem_ac = {}
rem_wa = {}
for _ in range(sub_num):
    problem, result = input().split()
    # すでに問題を提出していたら
    if problem in rem_ac.keys():
        # 1ならすでにACしている
        if rem_ac[problem] == 1:
            continue
        # ACしてないなら
        else:
            if result == 'WA':
                rem_wa[problem] += 1
                wa += 1
            else:
                ac += 1
                rem_ac[problem] = 1
    # 初めて提出するなら
    else:
        rem_ac[problem] = 0
        rem_wa[problem] = 0
        if result == 'WA':
            rem_wa[problem] += 1
            wa += 1
        else:
            ac += 1
            rem_ac[problem] = 1

for key, value in rem_ac.items():
    if value == 0:
        wa -= rem_wa[key]

print(ac, wa)

