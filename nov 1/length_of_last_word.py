n = int(input("Enter number of words: "))
words = []

for i in range(n):
    word = input("Enter word: ")
    words.append(word)

prefix = words[0]

for i in range(1, n):
    while words[i][:len(prefix)] != prefix:
        prefix = prefix[:-1]

        if prefix == "":
            break

    if prefix == "":
        break

print("Longest common prefix:", prefix)