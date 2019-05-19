s = input()

first = int(s[:2])
second = int(s[2:])

if 1 <= first <= 12 and 1 <= second <= 12:
    print('AMBIGUOUS')
elif 1 <= first <= 12:
    print('MMYY')
elif 1 <= second <= 12:
    print('YYMM')
else:
    print('NA')

