count = int(input("Enter number of words: "))

word_list = []

for i in range(count):
    item = input("Enter word: ")
    word_list.append(item)

pattern = input("Enter pattern: ")

result = []

for word in word_list:

    if len(word) == len(pattern):

        forward = {}
        backward = {}
        valid = True

        for j in range(len(word)):
            x = word[j]
            y = pattern[j]

            if x in forward:
                if forward[x] != y:
                    valid = False
                    break
            else:
                forward[x] = y

            if y in backward:
                if backward[y] != x:
                    valid = False
                    break
            else:
                backward[y] = x

        if valid:
            result.append(word)

print("Output:", result)