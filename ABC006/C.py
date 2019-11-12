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

    # つるかめ算
    rem_legs_num = legs_num - (aged_leg * aged_num)
    # 全員が赤ちゃんだと
    baby_num = pepole_num - aged_num
    # 差分がいくつあるか
    diff_legs = abs(rem_legs_num - (baby_leg * baby_num))
    # 差分を埋める大人の人数を決める
    adult_num = diff_legs // (baby_leg - adult_leg)
    # 再度赤ちゃんの人数を決める
    baby_num = pepole_num - adult_num - aged_num
    sum_legs = baby_leg * baby_num + aged_leg * aged_num + adult_leg * adult_num
    if sum_legs == legs_num and \
            baby_num >= 0 and aged_num >= 0 and adult_num >= 0:
        print(adult_num, aged_num, baby_num)
        exit()
print(-1, -1, -1)

