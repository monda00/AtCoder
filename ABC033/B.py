n = int(input())
max_people = 0
sum_people = 0
for _ in range(n):
    tmp_city, tmp_people = input().split()
    if max_people < int(tmp_people):
        max_people = int(tmp_people)
        max_city = tmp_city
    sum_people += int(tmp_people)
if sum_people < 2 * max_people:
    print(max_city)
else:
    print('atcoder')

