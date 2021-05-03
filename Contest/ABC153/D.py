h = int(input())


def attack_num(hp):
    if hp == 1:
        return 1
    else:
        return 2 * attack_num(hp//2) + 1


ans = attack_num(h)

print(ans)
