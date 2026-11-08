sentence = input("Enter a sentence: ")

words = []
temp = ""

for ch in sentence:
    if ch != " ":
        temp = temp + ch
    else:
        if temp != "":
            words.append(temp)
            temp = ""

if temp != "":
    words.append(temp)

answer = []

i = len(words) - 1

while i >= 0:
    answer.append(words[i])
    i -= 1

result = " ".join(answer)

print("Reversed sentence:", result)