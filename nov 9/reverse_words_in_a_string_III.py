sentence = input("Enter a sentence: ")

words = sentence.split(" ")
answer = []

for word in words:
    rev = ""
    for ch in word:
        rev = ch + rev
    answer.append(rev)

result = " ".join(answer)

print("Output:", result)