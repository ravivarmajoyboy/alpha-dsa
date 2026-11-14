total = int(input("Enter number of words: "))

items = []

for i in range(total):
    name = input("Enter word: ")
    items.append(name)

suffix = ""
pos = 1

while True:
    if pos > len(items[0]):
        break

    ch = items[0][-pos]
    same = True

    for j in range(1, total):
        if pos > len(items[j]) or items[j][-pos] != ch:
            same = False
            break

    if same:
        suffix = ch + suffix
        pos = pos + 1
    else:
        break

print("Longest common suffix:", suffix)