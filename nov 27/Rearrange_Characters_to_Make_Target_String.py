

source = input("Enter source string: ")
target = input("Enter target string: ")

count = {}

for ch in source:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1

answer = True

for ch in target:
    if ch in count and count[ch] > 0:
        count[ch] = count[ch] - 1
    else:
        answer = False
        break

print("Output:", answer)