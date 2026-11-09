word = input("Enter a word: ")
letter = input("Enter a character: ")

pos = -1

for i in range(len(word)):
    if word[i] == letter:
        pos = i
        break

if pos != -1:
    rev_part = ""

    for j in range(pos, -1, -1):
        rev_part = rev_part + word[j]

    result = rev_part + word[pos + 1:]
else:
    result = word

print("Output:", result)