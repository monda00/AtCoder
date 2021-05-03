age, cost = map(int, input().split())

if age <= 5:
    print(0)
elif 6 <= age <= 12:
    print(int(cost/2))
else:
    print(cost)

