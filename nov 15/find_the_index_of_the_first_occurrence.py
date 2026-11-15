text = input("Enter main string: ")
word = input("Enter word to find: ")

answer = -1

if len(word) == 0:
    answer = 0
else:
    for i in range(len(text) - len(word) + 1):
        match = True

        for j in range(len(word)):
            if text[i + j] != word[j]:
                match = False
                break

        if match:
            answer = i
            break

print("Output:", answer)