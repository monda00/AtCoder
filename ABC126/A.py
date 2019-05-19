n, k = map(int, input().split())

string = input()
list_string = list(string)

list_string[k-1] = string[k-1].lower()
print("".join(list_string))

