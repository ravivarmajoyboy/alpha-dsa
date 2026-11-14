sentence = input("Enter a string: ")
prefix = input("Enter prefix: ")

found = True

if len(prefix) > len(sentence):
    found = False
else:
    for i in range(len(prefix)):
        if sentence[i] != prefix[i]:
            found = False
            break

print(found)