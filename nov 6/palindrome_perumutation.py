text = input("Enter string: ")

data = {}

for ch in text:
    if ch in data:
        data[ch] += 1
    else:
        data[ch] = 1

count = 0

for ch in data:
    if data[ch] % 2 != 0:
        count += 1

if count <= 1:
    print("True")
else:
    print("False")