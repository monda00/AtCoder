n = int(input())

i = 1
saveing = 0
while True:
    saveing += i
    if saveing >= n:
        print(i)
        exit()
    i += 1
