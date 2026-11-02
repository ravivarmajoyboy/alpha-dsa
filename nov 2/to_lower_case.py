word = input("Enter a string: ")

answer = []

for ch in word:
    if ord(ch) >= 65 and ord(ch) <= 90:
        answer.append(chr(ord(ch) + 32))
    else:
        answer.append(ch)

result = "".join(answer)

print("Lowercase:", result)