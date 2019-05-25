import numpy as np

card_num, ope_num = map(int, input().split())

int_cards = np.array(list(map(int, input().split())))

for _ in range(ope_num):
    num_can_select_cards, changed_int = map(int, input().split())
    for _ in range(num_can_select_cards):
        if int_cards.min() > changed_int:
            break
        else:
            int_cards[np.argmin(int_cards)] = changed_int

print(np.sum(int_cards))

