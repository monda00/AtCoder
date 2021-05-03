x = list(input())
m = int(input())


def change_nto10(num, b):
    n = 0
    numlist = list(str(num))
    while(numlist):
        n *= b
        n += int(numlist.pop(0))
    return n


first_d = int(max(x))
X = int(''.join(x))

ans = 0
if len(x) == 1:
    if X > m:
        ans = 0
    else:
        ans = 1
else:
    start_d = first_d
    end_d = 10**60+1
    while (end_d-start_d) > 1:
        d = (start_d + end_d) // 2
        t = int(change_nto10(X, d))
        if t > m:
            end_d = d
        else:
            start_d = d
    ans = start_d - first_d

print(ans)
