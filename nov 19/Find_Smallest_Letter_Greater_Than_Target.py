letters = input("Enter sorted letters: ")
target = input("Enter target letter: ")

low = 0
high = len(letters) - 1
answer = letters[0]

while low <= high:
    mid = low + (high - low) // 2

    if letters[mid] > target:
        answer = letters[mid]
        high = mid - 1
    else:
        low = mid + 1

print("Output:", answer)