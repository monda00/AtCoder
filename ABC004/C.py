n = int(input())
card_li = ['1', '2', '3', '4', '5', '6']

n = n % 30
for i in range(n):
    tmp = card_li[i % 5]
    card_li[i % 5] = card_li[(i % 5) + 1]
    card_li[(i % 5) + 1] = tmp
print(''.join(card_li))

