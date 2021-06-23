input_int = input()

if input_int[0] == '-':
    reverse_int = '-' + input_int[:0:-1]
else:
    reverse_int = input_int[::-1]

print(reverse_int)
