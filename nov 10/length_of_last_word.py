sentence = input("Enter a sentence: ")

count = 0
i = len(sentence) - 1

while i >= 0 and sentence[i] == " ":
    i = i - 1

while i >= 0 and sentence[i] != " ":
    count = count + 1
    i = i - 1

print("Length of last word:", count)