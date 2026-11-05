text = input("Enter a string: ")

size = len(text)
answer = 0

for pos in range(size):

    # Odd length
    left = pos
    right = pos

    while left >= 0 and right < size:
        if text[left] == text[right]:
            answer += 1
            left -= 1
            right += 1
        else:
            break

    # Even length
    left = pos
    right = pos + 1

    while left >= 0 and right < size:
        if text[left] == text[right]:
            answer += 1
            left -= 1
            right += 1
        else:
            break

print("Number of palindromic substrings:", answer)