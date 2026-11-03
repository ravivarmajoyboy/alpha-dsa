text = input("Enter a string: ")

letters = {}

for ch in text:
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1

found = False

for i in range(len(text)):
    if letters[text[i]] == 1:
        print("First unique character:", text[i])
        print("Index:", i)
        found = True
        break

if found == False:
    print("No unique character found")