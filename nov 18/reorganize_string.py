word = input("Enter a string: ")

count = {}

for ch in word:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1

answer = ""
previous = ""

for i in range(len(word)):

    best = ""
    highest = 0

    for ch in count:
        if count[ch] > highest and ch != previous:
            highest = count[ch]
            best = ch

    if best == "":
        answer = ""
        break

    answer = answer + best
    count[best] = count[best] - 1
    previous = best

print("Output:", answer)