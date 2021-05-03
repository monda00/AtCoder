import itertools

switch_num, lights_num = map(int, input().split())

k_list = []
s_list = []
for _ in range(lights_num):
    k, *s = map(int, input().split())
    k_list.append(k)
    s_list.append(s)

p_list = list(map(int, input().split()))

for i in itertools.permutations([True, False], r=switch_num):
    print(i)

