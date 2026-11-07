word = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in word:

    if 'A' <= ch <= 'Z':
        ch = chr(ord(ch) + 32)

    if 'a' <= ch <= 'z':
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)