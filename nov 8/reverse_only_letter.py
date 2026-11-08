word = input("Enter a string: ")

letters = []

for ch in word:
    letters.append(ch)

left = 0
right = len(letters) - 1

while left < right:

    if not (('a' <= letters[left] <= 'z') or
            ('A' <= letters[left] <= 'Z')):
        left += 1

    elif not (('a' <= letters[right] <= 'z') or
              ('A' <= letters[right] <= 'Z')):
        right -= 1

    else:
        temp = letters[left]
        letters[left] = letters[right]
        letters[right] = temp

        left += 1
        right -= 1

result = "".join(letters)

print("Reversed letters:", result)