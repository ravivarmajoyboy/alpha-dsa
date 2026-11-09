text = input("Enter a string: ")

letters = list(text)

vowels = "aeiouAEIOU"

left = 0
right = len(letters) - 1

while left < right:

    if letters[left] not in vowels:
        left = left + 1

    elif letters[right] not in vowels:
        right = right - 1

    else:
        temp = letters[left]
        letters[left] = letters[right]
        letters[right] = temp

        left = left + 1
        right = right - 1

result = ""

for ch in letters:
    result = result + ch

print("Output:", result)