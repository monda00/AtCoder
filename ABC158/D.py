first_step_string = input()
query_num = int(input())
query_li = list()
for _ in range(query_num):
    query_li.append(input().split())

ans = first_step_string
rev_flag = False
for query in query_li:
    if query[0] == '1':
        rev_flag = not rev_flag
    elif (query[1] == '1' and rev_flag) or (query[1] == '2' and not rev_flag):
        ans += query[2]
    else:
        ans = query[2] + ans

if rev_flag:
    print(ans[::-1])
else:
    print(ans)
