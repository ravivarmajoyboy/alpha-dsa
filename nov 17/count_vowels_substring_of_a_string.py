text = input("Enter a string: ")

vowels = "aeiou"
total = 0

for i in range(len(text)):
    seen = {}

    for j in range(i, len(text)):
        ch = text[j]

        if ch not in vowels:
            break

        seen[ch] = 1

        if len(seen) == 5:
            total = total + 1

print("Output:", total)