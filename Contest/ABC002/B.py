def is_vowel(c):
    if c == 'a' or c == 'i' or c == 'u' or c == 'e' or c == 'o':
        return True
    else:
        return False

s = input()

ans_s = ''
for c in s:
    if is_vowel(c):
        continue
    else:
        ans_s += c
print(ans_s)

