first = input("Enter original string: ")
second = input("Enter rotated string: ")

found = False

if len(first) == len(second):
    n = len(first)

    if n == 0:
        found = True
    else:
        for i in range(n):
            match = True

            for j in range(n):
                pos = (i + j) % n

                if first[pos] != second[j]:
                    match = False
                    break

            if match:
                found = True
                break

print("Output:", found)
