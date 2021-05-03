import itertools

n = int(input())
str_n = str(n)

if n % 3 == 0:
    print(0)
    exit()

digits = [i for i in range(len(str_n))]

for i in range(len(str_n)-1):
    con = list(itertools.combinations(digits, i+1))
    for c in con:
        sub_n = str()
        for j in range(len(str_n)):
            if j not in c:
                sub_n += str_n[j]
        if int(sub_n) % 3 == 0:
            print(i+1)
            exit()

print(-1)
