char_num, changed_limit = map(int, input().split())
input_string = list(input())
changed_num = 0

for i, c in enumerate(input_string):
    if changed_num < changed_limit and input_string[i] != min(input_string[i:]):
        print(input_string.index(min(input_string[i:])))
        print(i)
        print(input_string)
        tmp = input_string[i]
        print('tmp = {}'.format(tmp))
        print('input_string[{}] = {}'.format(i, input_string[i]))
        input_string[i] = input_string[input_string.index(min(input_string[i:]))]
        min_index = input_string.index(min(input_string[i:]))
        print('input_string[{}] = {}'.format(i, input_string[i]))
        print('input_string[{}] = {}'.format(input_string.index(min(input_string[i:])), input_string[input_string.index(min(input_string[i:]))]))
        print('min_index = {}'.format(min_index))
        input_string[min_index] = tmp
        print('input_string[{}] = {}'.format(input_string.index(min(input_string[i:])), input_string[input_string.index(min(input_string[i:]))]))
        print(input_string.index(min(input_string[i:])))
        print(i)
        print(input_string)
        changed_num += 2

print(''.join(input_string))

