'''
[C - N進数](https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_c)
'''

a = int(input())

for i in range(10, 10001):
    num = 0
    str_i = str(i)
    len_i = len(str_i)
    for j in range(len_i):
        num += i**j * int(str_i[len_i - 1 - j])
    if num == a:
        print(i)
        exit()

print(-1)
