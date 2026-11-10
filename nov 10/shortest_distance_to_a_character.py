word = input("Enter a string: ")
ch = input("Enter a character: ")

answer = []

for i in range(len(word)):
    small = len(word)

    for j in range(len(word)):
        if word[j] == ch:
            distance = i - j

            if distance < 0:
                distance = -distance

            if distance < small:
                small = distance

    answer.append(small)

print("Output:", answer)