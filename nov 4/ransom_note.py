note = input("Enter ransom note: ")
magazine = input("Enter magazine string: ")

letters = {}

for ch in magazine:
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1

possible = True

for ch in note:
    if ch in letters and letters[ch] > 0:
        letters[ch] -= 1
    else:
        possible = False
        break

if possible:
    print("Can make ransom note")
else:
    print("Cannot make ransom note")