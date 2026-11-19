first = input("Enter first string: ")
second = input("Enter second string: ")

answer = ""

limit = len(first)

if len(second) < limit:
    limit = len(second)

found = False

for i in range(limit):
    if first[i] < second[i]:
        answer = "First string is smaller"
        found = True
        break

    elif first[i] > second[i]:
        answer = "Second string is smaller"
        found = True
        break

if not found:
    if len(first) < len(second):
        answer = "First string is smaller"
    elif len(first) > len(second):
        answer = "Second string is smaller"
    else:
        answer = "Both strings are equal"

print("Output:", answer)