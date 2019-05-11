import numpy as np

n = int(input())
a_arr = np.array(list(map(int, input().split())))

alice_point = 0
bob_point = 0

while np.any(a_arr > 0):
    alice_point += a_arr[a_arr.argmax()]
    a_arr[a_arr.argmax()] = -1
    if np.any(a_arr > 0):
        bob_point += a_arr[a_arr.argmax()]
        a_arr[a_arr.argmax()] = -1

print(alice_point - bob_point)

