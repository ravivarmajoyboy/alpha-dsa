
binary = input("Enter binary string: ")

change1 = 0
change2 = 0

for i in range(len(binary)):

    if i % 2 == 0:
        if binary[i] != "0":
            change1 = change1 + 1

        if binary[i] != "1":
            change2 = change2 + 1

    else:
        if binary[i] != "1":
            change1 = change1 + 1

        if binary[i] != "0":
            change2 = change2 + 1

if change1 < change2:
    answer = change1
else:
    answer = change2

print("Output:", answer)