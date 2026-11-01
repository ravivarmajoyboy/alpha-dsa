sentence = input("Enter a sentence: ")

i = len(sentence) - 1
count = 0

while i >= 0 and sentence[i] == " ":
    i -= 1

while i >= 0 and sentence[i] != " ":
    count += 1
    i -= 1

print("Length of last word:", count)