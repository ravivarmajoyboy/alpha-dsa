text = input("Enter a title: ")

answer = []
word = []
count = 0

for ch in text + " ":
    if ch != " ":
        word.append(ch)
        count += 1
    else:
        if count > 0:
            if count <= 2:
                for c in word:
                    if ord(c) >= 65 and ord(c) <= 90:
                        answer.append(chr(ord(c) + 32))
                    else:
                        answer.append(c)
            else:
                for i in range(count):
                    c = word[i]

                    if i == 0:
                        if ord(c) >= 97 and ord(c) <= 122:
                            answer.append(chr(ord(c) - 32))
                        else:
                            answer.append(c)
                    else:
                        if ord(c) >= 65 and ord(c) <= 90:
                            answer.append(chr(ord(c) + 32))
                        else:
                            answer.append(c)

            word = []
            count = 0

        answer.append(" ")

result = "".join(answer)
print("Capitalized title:", result[:-1])