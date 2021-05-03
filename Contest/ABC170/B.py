x, y = map(int, input().split())

all_crane_num = x * 2
diff = y - all_crane_num

turtle_num = int(diff / 2)
crane_num = x - turtle_num

if turtle_num >= 0 and crane_num >= 0 and turtle_num*4 + crane_num*2 == y:
    print('Yes')
else:
    print('No')
