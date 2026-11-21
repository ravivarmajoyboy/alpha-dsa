
sentence = input("Enter a sentence: ")

count = 0
inside = False

for ch in sentence:
    if ch != " " and ch != "\t" and ch != "\n":
        if inside == False:
            count = count + 1
            inside = True
    else:
        inside = False

print("Output:", count)