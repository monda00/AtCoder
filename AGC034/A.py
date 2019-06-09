box_num, a_start, b_start, a_end, b_end = map(int, input().split())
box = input()
a_now = a_start
b_now = b_start

def a_one(a_now, b_now):
    a_now += 1

    if(a_now > a_end or b_now > b_end or a_now > box_num):
        return
    if(a_now == a_end and b_now == b_end):
        print("Yes")
        exit()
    if(box[a_now-1] == '#' or a_now == b_now):
        return

    a_one(a_now, b_now)
    a_two(a_now, b_now)
    b_one(a_now, b_now)
    b_two(a_now, b_now)

def a_two(a_now, b_now):
    a_now += 2

    if(a_now > a_end or b_now > b_end or a_now > box_num):
        return
    if(a_now == a_end and b_now == b_end):
        print("Yes")
        exit()
    if(box[a_now-1] == '#' or a_now == b_now):
        return

    a_one(a_now, b_now)
    a_two(a_now, b_now)
    b_one(a_now, b_now)
    b_two(a_now, b_now)

def b_one(a_now, b_now):
    b_now += 1

    if(a_now > a_end or b_now > b_end or b_now > box_num):
        return
    if(a_now == a_end and b_now == b_end):
        print("Yes")
        exit()
    if(box[b_now-1] == '#' or a_now == b_now):
        return

    a_one(a_now, b_now)
    a_two(a_now, b_now)
    b_one(a_now, b_now)
    b_two(a_now, b_now)

def b_two(a_now, b_now):
    b_now += 2

    if(a_now > a_end or b_now > b_end or b_now > box_num):
        return
    if(a_now == a_end and b_now == b_end):
        print("Yes")
        exit()
    if(box[b_now-1] == '#' or a_now == b_now):
        return

    a_one(a_now, b_now)
    a_two(a_now, b_now)
    b_one(a_now, b_now)
    b_two(a_now, b_now)

a_one(a_now, b_now)
a_two(a_now, b_now)
b_one(a_now, b_now)
b_two(a_now, b_now)

print("No")

