pepole_num, legs_num = map(int, input().split())
baby_leg = 4
aged_leg = 3
adult_leg = 2

for aged_num in range(pepole_num + 1):
    # すでにlegs_nmを超えていたら
    if aged_num * aged_leg > legs_num:
        break
    # 残りが奇数だと4と2では構成できない
    if (legs_num - aged_num * aged_leg) % 2 == 1:
        continue
    for baby_num in range(pepole_num - aged_num + 1):
        adult_num = pepole_num - baby_num - aged_num
        sum_legs = baby_num * baby_leg + aged_num * aged_leg + \
            adult_num * adult_leg
        # すでにlegs_nmを超えていたら
        if sum_legs > legs_num:
            break
        if sum_legs == legs_num:
            print(adult_num, aged_num, baby_num)
            exit()
print(-1, -1, -1)

