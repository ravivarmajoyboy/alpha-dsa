text = input("Enter main string: ")

n = int(input("Enter number of words: "))
words = []

for i in range(n):
    item = input("Enter word: ")
    words.append(item)

answer = ""

for word in words:
    i = 0
    j = 0

    while i < len(text) and j < len(word):
        if text[i] == word[j]:
            j = j + 1

        i = i + 1

    if j == len(word):
        if len(word) > len(answer):
            answer = word
        elif len(word) == len(answer):
            if word < answer:
                answer = word

print("Output:", answer)