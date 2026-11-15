text = input("Enter a string: ")

found = False
n = len(text)

for size in range(1, n):
    if n % size == 0:
        part = text[:size]
        match = True

        for i in range(0, n, size):
            for j in range(size):
                if text[i + j] != part[j]:
                    match = False
                    break

            if not match:
                break

        if match:
            found = True
            break

print("Output:", found)