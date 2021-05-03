import math
# python3ではroundが最近接偶数に丸められてしまうため関数を作成
def round(x,d=0):
    p=10**d
    return (x*p*2+1)//2/p

wind_deg, wind_dis = map(int, input().split())
wind_spd = round(wind_dis / 60.0, 1)

# 風力
if 0.0 <= wind_spd <= 0.2:
    wind_pow = 0
elif 0.3 <= wind_spd <= 1.5:
    wind_pow = 1
elif 1.6 <= wind_spd <= 3.3:
    wind_pow = 2
elif 3.4 <= wind_spd <= 5.4:
    wind_pow = 3
elif 5.5 <= wind_spd <= 7.9:
    wind_pow = 4
elif 8.0 <= wind_spd <= 10.7:
    wind_pow = 5
elif 10.8 <= wind_spd <= 13.8:
    wind_pow = 6
elif 13.9 <= wind_spd <= 17.1:
    wind_pow = 7
elif 17.2 <= wind_spd <= 20.7:
    wind_pow = 8
elif 20.8 <= wind_spd <= 24.4:
    wind_pow = 9
elif 24.5 <= wind_spd <= 28.4:
    wind_pow = 10
elif 28.5 <= wind_spd <= 32.6:
    wind_pow = 11
elif 32.7 <= wind_spd:
    wind_pow = 12

# 風向
if wind_pow == 0:
    wind_dir = 'C'
elif 112.5 <= wind_deg < 337.5:
    wind_dir = 'NNE'
elif 337.5 <= wind_deg < 562.5:
    wind_dir = 'NE'
elif 562.5 <= wind_deg < 787.5:
    wind_dir = 'ENE'
elif 787.5 <= wind_deg < 1012.5:
    wind_dir = 'E'
elif 1012.5 <= wind_deg < 1237.5:
    wind_dir = 'ESE'
elif 1237.5 <= wind_deg < 1462.5:
    wind_dir = 'SE'
elif 1462.5 <= wind_deg < 1687.5:
    wind_dir = 'SSE'
elif 1687.5 <= wind_deg < 1912.5:
    wind_dir = 'S'
elif 1912.5 <= wind_deg < 2137.5:
    wind_dir = 'SSW'
elif 2137.5 <= wind_deg < 2362.5:
    wind_dir = 'SW'
elif 2362.5 <= wind_deg < 2587.5:
    wind_dir = 'WSW'
elif 2587.5 <= wind_deg < 2812.5:
    wind_dir = 'W'
elif 2812.5 <= wind_deg < 3037.5:
    wind_dir = 'WNW'
elif 3037.5 <= wind_deg < 3262.5:
    wind_dir = 'NW'
elif 3262.5 <= wind_deg < 3487.5:
    wind_dir = 'NNW'
else:
    wind_dir = 'N'

print(wind_dir, wind_pow)

