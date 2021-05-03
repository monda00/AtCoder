t_hp, t_att, a_hp, a_att = map(int, input().split())

while(t_hp > 0 and a_hp > 0):
    a_hp -= t_att
    t_hp -= a_att

if a_hp <= 0:
    print('Yes')
else:
    print('No')
