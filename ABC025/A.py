s = input()
n = int(input())

i = 1
for c1 in s:
    for c2 in s:
        if i == n:
            print(c1 + c2)
            exit()
        i += 1

