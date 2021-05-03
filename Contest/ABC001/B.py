x_meter = int(input())
x_km = x_meter / float(1000)

if x_km < 0.1:
    print('00')
elif 0.1 <= x_km <= 5:
    if x_km * 10 < 10:
        print('0' + str(int(x_km * 10)))
    else:
        print(int(x_km * 10))
elif 6 <= x_km <= 30:
    print(int(x_km + 50))
elif 35 <= x_km <= 70:
    print(int((x_km - 30) / 5 + 80))
else:
    print(89)

