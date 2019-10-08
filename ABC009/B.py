import numpy as np

n = int(input())
menu_list = []

for _ in range(n):
    menu_list.append(int(input()))

money_set = np.array(list(set(menu_list)))
money_sorted_ind = money_set.argsort()[::-1]

print(money_set[money_sorted_ind[1]])

