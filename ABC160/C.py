lake_m, house_num = map(int, input().split())
house_m_li = list(map(int, input().split()))

house_between_distance = list()

for i in range(house_num):
    if i == 0:
        house_between_distance.append(house_m_li[i] + (lake_m - house_m_li[-1]))
    else:
        house_between_distance.append(house_m_li[i] - house_m_li[i-1])

print(lake_m - max(house_between_distance))
