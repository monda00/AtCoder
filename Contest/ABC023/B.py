n = int(input())
s = input()

if n % 2 == 0:
    print(-1)
else:
    half_index = n // 2
    if s[half_index] != 'b':
        print(-1)
        exit()
    s_first = s[:half_index]
    while(len(s_first) > 1):
        if ((s_first[0] == 'a' and s_first[1] == 'b') or \
                (s_first[0] == 'b' and s_first[1] == 'c') or \
                (s_first[0] == 'c' and s_first[1] == 'a')):
            s_first = list(s_first)
            s_first.pop(0)
            s_first = "".join(s_first)
        else:
            print(-1)
            exit()
    s_second = s[half_index+1:]
    while(len(s_second) > 1):
        if ((s_second[0] == 'a' and s_second[1] == 'b') or \
                (s_second[0] == 'b' and s_second[1] == 'c') or \
                (s_second[0] == 'c' and s_second[1] == 'a')):
            s_second = list(s_second)
            s_second.pop(0)
            s_second = "".join(s_second)
        else:
            print(-1)
            exit()
    print(half_index)

