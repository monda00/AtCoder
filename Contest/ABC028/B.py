s = input()
cout_c = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
for c in s:
    cout_c[c] += 1
print(str(cout_c["A"]) + " " + str(cout_c["B"]) + " " + str(cout_c["C"]) + " " + str(cout_c["D"]) + " " + str(cout_c["E"]) + " " + str(cout_c["F"]))
# print(*cout_c.values())

