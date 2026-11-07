text = input("Enter a sentence: ")

letters = []

for ch in text:
    if 'A' <= ch <= 'Z':
        ch = chr(ord(ch) + 32)

    if 'a' <= ch <= 'z':
        if ch not in letters:
            letters.append(ch)

if len(letters) == 26:
    print("Pangram")
else:
    print("Not Pangram")