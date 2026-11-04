n = int(input("Enter number of words: "))
words = []

for i in range(n):
    word = input("Enter word: ")
    words.append(word)

common = {}

for ch in words[0]:
    if ch in common:
        common[ch] += 1
    else:
        common[ch] = 1

for i in range(1, n):
    current = {}

    for ch in words[i]:
        if ch in current:
            current[ch] += 1
        else:
            current[ch] = 1

    for ch in common:
        if ch in current:
            if current[ch] < common[ch]:
                common[ch] = current[ch]
        else:
            common[ch] = 0

answer = []

for ch in common:
    for i in range(common[ch]):
        answer.append(ch)

print("Common characters:", answer)