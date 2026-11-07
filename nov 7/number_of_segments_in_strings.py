sentence = input("Enter a sentence: ")

count = 0
inside = False

for ch in sentence:
    if ch != " ":
        if inside == False:
            count += 1
            inside = True
    else:
        inside = False

print("Number of segments:", count)