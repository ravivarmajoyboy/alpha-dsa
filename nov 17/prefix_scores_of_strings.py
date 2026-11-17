n = int(input("Enter number of words: "))

words = []

for i in range(n):
    name = input("Enter word: ")
    words.append(name)

scores = []

for i in range(n):
    total = 0

    for j in range(n):
        count = 0
        a = words[i]
        b = words[j]

        limit = len(a)

        if len(b) < limit:
            limit = len(b)

        for k in range(limit):
            if a[k] == b[k]:
                count = count + 1
            else:
                break

        total = total + count

    scores.append(total)

print("Output:", scores)