restrunt_num = int(input())

restrunt_list = []
for i in range(1, restrunt_num+1):
    city, point = input().split()
    restrunt_list.append([city, int(point), i])

sorted_list = sorted(restrunt_list, key=lambda x: (x[0], -x[1]))
for r in sorted_list:
    print(r[2])

