n = int(input("Enter number of words: "))

words = []

for i in range(n):
    item = input("Enter word: ")
    words.append(item)

prefix = words[0]

for i in range(1, n):
    while len(prefix) > 0:
        if words[i][:len(prefix)] == prefix:
            break
        prefix = prefix[:-1]

print("Longest common prefix:", prefix)