char_num, changed_limit = map(int, input().split())
input_string = list(input())
original_string = input_string
changed_string = list()

for i, c in enumerate(input_string):
    if i < changed_limit:
        changed_string += min(original_string)
        original_string.remove(min(original_string))

print(original_string)
print(changed_string)
result = changed_string + original_string
print(''.join(result))

