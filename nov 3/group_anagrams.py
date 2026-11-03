n = int(input("Enter number of words: "))
words = []

for i in range(n):
    name = input("Enter word: ")
    words.append(name)

groups = {}
result = []

for word in words:
    count = {}

    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    key = tuple(sorted(count.items()))

    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]

for key in groups:
    result.append(groups[key])

print("Grouped Anagrams:")

for group in result:
    print(group)